import sys
from lib import utils, data_loader, data_writer
from lib.config_loader import get_chat_conf
from lib.data_cleansing import CleansedDf
from lib.transformations import Transform
from lib.logger import Log4j

if __name__ == '__main__':

    if len(sys.argv) < 3:
        print("Usage: ChatAnalysis {local, qa, prod} : Arguments are missing")
        sys.exit(-1)

    job_run_env = sys.argv[1].upper()
    source_file_env = sys.argv[2].upper()

    print("Creating Spark Session")
    spark = utils.get_spark_session(job_run_env)
    logger = Log4j(spark)

    print("Get the Source Files")
    conf_local = get_chat_conf(source_file_env)
    chatFile = conf_local.get("file.path.chat")
    categoryFile = conf_local.get("file.path.category")

    logger.info("Reading Chat Records DF")
    chat_df = data_loader.read_chat(spark, chatFile, logger)

    logger.info("Reading Category Records DF")
    category_df = data_loader.read_category(spark, categoryFile, logger)

    logger.info("Data Cleansing in progress for removing bad data")
    cleanser = CleansedDf(chat_df, category_df)
    cleanedChatDf, cleanedCategoryDf = cleanser.run_all(logger)

    logger.info("Data Transformation to get metrics for analysis")
    transformed_data = Transform(cleanedChatDf)
    analysis_output = transformed_data.analysis(logger)

    logger.info("Write analysis output to chat_analysis folder")
    data_writer.save_all_outputs(analysis_output, logger)

    logger.info("Successfully Completed the Analysis of Customer Chats")



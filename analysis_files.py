import logging
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from numpy import random
import sys


logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

file_handler = logging.FileHandler('programming.log')
file_handler.setLevel(logging.INFO)

formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)


def main():
    file_input1 = input("just you normal scans [columns - shape - dtypes - info - head - isnul [Click on Number 1:]... ")
    
    if file_input1 == '1':
        file_path = input("Enter file path... ")
        
        if file_path:
            try:
                df = pd.read_csv(file_path)
                logger.info("Running %s" % file_input1)
                
                head_scan = input('How scan HEAD? ')
                logger.info(f"First {head_scan} rows of data frame:\n%s", df.head(int(head_scan)))
                
                logger.info("Column names:\n%s", df.columns)
                logger.info("Column types:\n%s", df.shape)
                logger.info("Column types:\n%s", df.dtypes)
                
                info_scans = input('How scan INFO ?')
                logger.info(f"Column types:\n%s", df.info(max_cols=int(info_scans)))

                isnull_scans = input("Is null scan number... ")
                logger.info(f"Column types {isnull_scans} :\n%s", df.isnull(int(isnull_scans)).sum())


                
            except Exception as error:
                logger.error("Error Loading data frame")
                logger.error("Error: %s" % error)

            finally:
                logger.info("Exiting %s" % file_input1)
    else:
        logger.warning("Invalid input. Please enter '1' to continue with the process.")

def main2():
    file_input2 = input("If you want the appearance of cvs and other file, [Click on number 2]... ")
    
    if file_input2 == '2' :
        file_path2 = input("Enter file path... ")
    
        if file_path2:
            try:
                df = pd.read_csv(file_path2)
            
                """
                
                    This is the Displot of the Plot :
                
                """

                graph_type = input("Enter the type of graph you want to see (displot, barplot, distplot etc.): ")
                #displot_input = input("If you want to draw a Scatter Plot, press enter if you do not want to, [Y] if you do not want to. ")
                #if displot_input == 'Y':
                if graph_type == 'displot':
                    sns.displot(df['Price'])
                    plt.show()
                    logger.info("Exiting Program...")
                    sys.exit()
                    

                """
                
                This is Random Uniform distribution function in distplot
                

                """
                if graph_type == 'distplot':
                    sns.distplot(random.uniform(size=1000), hist=False)
                    plt.show()
                    logger.info("Exiting Program...")
                    sys.exit()


                """
                
                This is Barplot with the xlabel for the ylabel fonction
                
                """
                if graph_type == 'barplot':
                    sns.barplot(x = df[f'{xlabel}'], y = df[f'{ylabel}'])
                    plt.show()

                    barplot_input = input("If you want to Barplot with the xlabel for the ylabel [Y]...")

                    if barplot_input == "Y":
                        xlabel = input("Enter the xlabel name... ")
                        ylabel = input("Enter the ylabel name... ")
                    logger.info("Exiting Program...")
                    sys.exit()

                """
                    
                    All errors msj
                     
                """
            except Exception as error:
                logger.error("Error Loading data frame")
                logger.error("Error: %s" % error)

            finally:
                logger.warning("Exiting %s" % file_input2)



if __name__ == '__main__':
    main()
    main2()

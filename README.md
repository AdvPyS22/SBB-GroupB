# SBB-GroupB
SBB data analysis 
# introduction
We analyze the SBB dataset and create the code that users can use directly to get what they want, like if they can enter a station name, then they run the code, they will get all the clock statistics information. Also, users can dynamically select which information to plot and enter new information in the databases.  

# Usage
- Download the zip file. Decompressing the file. Enter the file.
- check the requirement.txt, and check if you have all the package you needed in your computer. Or you can **pip install -r requirement.txt**
- Open **main.py** file. And run it.
- You will be asked to input the station name you are interested and you will get the statistics information, a pdf file(named 'input name'-output.pdf),about clock. Don't care about capitalization and spaces before and after characters of the name.  
For example, if you are interested in 'bern' station clock information. You can input 'Bern' '  BERN' or "BERn'. Then you will get a pdf file, called **Bern-output.pdf**, which shows you statistics information about clock.
- And you also will a pie plot that shows ramps/stairs information. Also in order to users explore the data conveniently, you can copy the print text.
- Next step, enter the information you are interested in. And choose the result's type. We offer three different ways，'pie', 'bar' or 'all', to show the result.
- Then you will be asked to whether enter the new information or not. Enter **y** to continue the step. And according to the hint, continue the following steps.

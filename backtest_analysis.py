import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
from PIL import Image




st.set_page_config(layout="wide",page_icon="🧊",initial_sidebar_state="auto")
st.set_option('deprecation.showPyplotGlobalUse', False)

st.sidebar.title("Stock Backtest Anlaysis")
st.sidebar.image('https://cdn.corporatefinanceinstitute.com/assets/backtesting1.jpeg')


# removing streamlit 
hide_st_style = """
			<style>
			#MainMenu {visibility: hidden;}
			footer {visibility: hidden;}
			header {visibility: hidden;}
			</style>
			"""

stock_list = ['LAURUSLABS','ASHOKLEY', 'AXISBANK', 'CUB', 'APOLLOTYRE', 'IBULHSGFIN', 'IEX', 'SUNPHARMA', 'INTELLECT', 'M&M', 'MRF', 'IGL', 'HCLTECH', 'INDUSTOWER', 'TORNTPHARM', 'AUBANK', 'HDFCBANK', 'HDFCLIFE', 'CROMPTON', 'BHEL', 'NMDC', 'IPCALAB', 'ALKEM', 'ZEEL', 'ITC', 'MCDOWELL-N', 'LALPATHLAB', 'ADANIENT', 'MARICO', 'NATIONALUM', 'DIXON', 'DEEPAKNTR', 'NESTLEIND', 'BOSCHLTD', 'TATACHEM', 'ESCORTS', 'MARUTI', 'VOLTAS', 'COALINDIA', 'SHREECEM', 'LTTS', 'CONCOR', 'GUJGASLTD', 'PIIND', 'BAJFINANCE', 'COLPAL', 'ICICIBANK', 'CIPLA', 'JUBLFOOD', 'PETRONET', 'BERGEPAINT', 'FEDERALBNK', 'LT', 'PERSISTENT', 'APOLLOHOSP', 'DIVISLAB', 'LICHSGFIN', 'JKCEMENT', 'GODREJCP', 'BAJAJ-AUTO', 'INFY', 'HINDPETRO', 'ASTRAL', 'BPCL', 'ASIANPAINT', 'GRANULES', 'BANDHANBNK', 'HINDUNILVR', 'PAGEIND', 'IDFCFIRSTB', 'ATUL', 'MUTHOOTFIN', 'JSWSTEEL', 'SYNGENE', 'AUROPHARMA', 'POWERGRID', 'MANAPPURAM', 'CHOLAFIN', 'INDUSINDBK', 'SUNTV', 'INDIGO', 'ABFRL', 'NAVINFLUOR', 'IDFC', 'BSOFT', 'PEL', 'RECLTD', 'ABBOTINDIA', 'TCS', 'OFSS', 'BHARATFORG', 'HAVELLS', 'BANKBARODA', 'LUPIN', 'TORNTPOWER', 'HINDCOPPER', 'HAL', 'BEL', 'ABCAPITAL', 'ABB', 'TATACONSUM', 'KOTAKBANK', 'PNB', 'DELTACORP', 'TRENT', 'HINDALCO', 'TATACOMM', 'LTIM', 'MGL', 'SBIN', 'EICHERMOT', 'RELIANCE', 'RBLBANK', 'UBL', 'INDHOTEL', 'BRITANNIA', 'BALKRISIND', 'NTPC', 'DABUR', 'ULTRACEMCO', 'ONGC', 'TVSMOTOR', 'GLENMARK', 'ICICIPRULI', 'RAMCOCEM', 'HEROMOTOCO', 'GRASIM', 'WHIRLPOOL', 'GAIL', 'IOC', 'SIEMENS', 'MPHASIS', 'GNFC', 'IDEA', 'BHARTIARTL', 'COROMANDEL', 'SHRIRAMFIN', 'BALRAMCHIN', 'CHAMBLFERT', 'AARTIIND', 'RAIN', 'OBEROIRLTY', 'TITAN', 'SRF', 'NAUKRI', 'ICICIGI', 'PVR', 'SBILIFE', 'ADANIPORTS', 'HDFCAMC', 'HDFC', 'MOTHERSON', 'MFSL', 'PIDILITIND', 'TATAMOTORS', 'ACC', 'L&TFH', 'GODREJPROP', 'COFORGE', 'FSL', 'MCX', 'BIOCON', 'VEDL', 'M&MFIN', 'SAIL', 'EXIDEIND', 'CANBK', 'WIPRO', 'DLF', 'CANFINHOME', 'JINDALSTEL', 'CUMMINSIND', 'TECHM', 'BATAINDIA', 'DRREDDY', 'AMBUJACEM', 'BAJAJFINSV', 'TATAPOWER', 'ZYDUSLIFE', 'INDIACEM', 'GMRINFRA', 'TATASTEEL', 'PFC', 'UPL', 'HONAUT']
stock = st.selectbox('Select Stock',sorted(stock_list))
csv_name = (stock + ".csv")


stock_df = pd.read_csv(csv_name)
stock_df['trail'] = stock_df['trail'] + "-" + stock_df['type']
stock_df['profit_or_loss'] = ['Profit' if x > 0 else 'Loss' for x in stock_df['p&l']]


option = st.sidebar.selectbox('Select One',['General Analysis','Conditional Anlaysis','EDA'])


if option == 'General Analysis':
	st.title("General Analysis")
	option = st.selectbox('Select Statistics Type',['sum','value_count','average'])

	if option == 'sum':
		sub_option = st.selectbox('Select Column',['buyprice','date', 'buytime', 'sl', 'type', 'stock', 'buyslpoints', 'tgt', 'buy1to1', 'buy1to2', 'buy1to3', 'buy1to4', 'buy1to5', 'buy1to6', 'buy1to7', 'buy1to8', 'buy1to9', 'sellprice', 'selltime', 'p&l', 'remarks', 'trail', 'sell1to1', 'sell1to2', 'sell1to3', 'sell1to4', 'sell1to5', 'sell1to6', 'sell1to7', 'sell1to8', 'sell1to9', 'sellslpoints', 'lot_size', 'day', 'month', 'nifty_open', 'nifty_prev_close', 'nifty_trend', 'trade_time', 'profit_or_loss'])
		sub_option = str(sub_option)
		st.subheader(stock_df[sub_option].sum())

	elif option == 'value_count':
		sub_option = st.selectbox('Select Column',['buyprice','date', 'buytime', 'sl', 'type', 'stock', 'buyslpoints', 'tgt', 'buy1to1', 'buy1to2', 'buy1to3', 'buy1to4', 'buy1to5', 'buy1to6', 'buy1to7', 'buy1to8', 'buy1to9', 'sellprice', 'selltime', 'p&l', 'remarks', 'trail', 'sell1to1', 'sell1to2', 'sell1to3', 'sell1to4', 'sell1to5', 'sell1to6', 'sell1to7', 'sell1to8', 'sell1to9', 'sellslpoints', 'lot_size', 'day', 'month', 'nifty_open', 'nifty_prev_close', 'nifty_trend', 'trade_time', 'profit_or_loss'])
		sub_option = str(sub_option)
		st.table(stock_df[sub_option].value_counts())

	else:
		sub_option = st.selectbox('Select Column',['buyprice','date', 'buytime', 'sl', 'type', 'stock', 'buyslpoints', 'tgt', 'buy1to1', 'buy1to2', 'buy1to3', 'buy1to4', 'buy1to5', 'buy1to6', 'buy1to7', 'buy1to8', 'buy1to9', 'sellprice', 'selltime', 'p&l', 'remarks', 'trail', 'sell1to1', 'sell1to2', 'sell1to3', 'sell1to4', 'sell1to5', 'sell1to6', 'sell1to7', 'sell1to8', 'sell1to9', 'sellslpoints', 'lot_size', 'day', 'month', 'nifty_open', 'nifty_prev_close', 'nifty_trend', 'trade_time', 'profit_or_loss'])
		sub_option = str(sub_option)
		st.subheader(stock_df[sub_option].mean())


elif option == 'Conditional Anlaysis':
	st.title("Conditional Analysis")
	st.subheader("Add Group By msethods")


else:
	st.title("Explanatory Data Aanalysis")
	eda_option = st.selectbox("Select Analysis Type",['Univariate Analysis', 'Bivariate Analysis', 'Multi-variate Analysis'])

	if eda_option == 'Univariate Analysis':
		column_option = st.selectbox("Select a column",['buyprice', 'date', 'buytime', 'sl', 'type', 'stock', 'buyslpoints', 'tgt', 'buy1to1', 'buy1to2', 'buy1to3', 'buy1to4', 'buy1to5', 'buy1to6', 'buy1to7', 'buy1to8', 'buy1to9', 'sellprice', 'selltime', 'p&l', 'remarks', 'trail', 'sell1to1', 'sell1to2', 'sell1to3', 'sell1to4', 'sell1to5', 'sell1to6', 'sell1to7', 'sell1to8', 'sell1to9', 'sellslpoints', 'lot_size', 'day', 'month', 'nifty_open', 'nifty_prev_close', 'nifty_trend', 'trade_time', 'profit_or_loss'])
		sub_option = st.selectbox("Select an Option",['Describe', 'Null Values', 'Data Distribution', 'Skewness', 'Outliars','Value counts','Percentage counts'])

		if sub_option == 'Describe':
			st.table(stock_df[column_option].describe())

		elif sub_option == 'Null Values':
			st.subheader("Total Null Values")
			st.write(stock_df[column_option].isnull().sum())
			st.subheader("Null Values Percentage")
			st.write(stock_df[column_option].isnull().sum()/len(stock_df[column_option]))

		elif sub_option == 'Data Distribution':
			st.subheader("Hist Plot")
			fig, ax = plt.subplots()
			ax.hist(stock_df[column_option], bins=20)
			st.pyplot(fig)


		elif sub_option == 'Skewness':
			st.write(sns.FacetGrid(stock_df).map(sns.kdeplot, column_option).add_legend())
			st.pyplot()

			skewness = stock_df[column_option].skew()
			if skewness > 1:
			    st.write('Highly Positively Skewed: ', skewness)
			
			elif skewness < 0:
			    st.write('Highly Negatively Skewed: ', skewness)
			
			elif abs(skewness) < 0.5:
			    st.write('Normally Distributed: ', skewness)
			
			else:
			    st.write('Moderately Skewed: ', skewness)



		elif sub_option == 'Outliars':
			st.write(sns.FacetGrid(stock_df).map(sns.boxplot, column_option).add_legend())
			st.pyplot()


		elif sub_option == 'Value counts':
			value_counting = (stock_df[column_option].value_counts())
			fig, ax = plt.subplots()
			ax.bar(value_counting.index, value_counting.values)

			ax.set_title(f"Value counts of {column_option} column")
			ax.set_xlabel(column_option)
			ax.set_ylabel("Count")
			st.pyplot(fig)


		elif sub_option == 'Percentage counts':
			value_counting = (stock_df[column_option].value_counts())
			fig = px.pie(names=value_counting.index, values=value_counting.values, labels=value_counting.index, hole=0.5,
            title="Value counts of 'Type' column")
			fig.update_traces(textposition='inside', textinfo='percent+label')
			st.plotly_chart(fig)


	elif eda_option == 'Bivariate Analysis':
		relation_type = st.selectbox('Choose Relationship between Data',['Numerical - Numerical','Categorical - Numerical', 'Categorical - Categorical'])
		
		if relation_type == 'Categorical - Categorical':
			options = ['buyprice', 'date', 'buytime', 'sl', 'type', 'stock', 'buyslpoints', 'tgt', 'buy1to1', 'buy1to2', 'buy1to3', 'buy1to4', 'buy1to5', 'buy1to6', 'buy1to7', 'buy1to8', 'buy1to9', 'sellprice', 'selltime', 'profit_or_loss', 'remarks', 'trail', 'sell1to1', 'sell1to2', 'sell1to3', 'sell1to4', 'sell1to5', 'sell1to6', 'sell1to7', 'sell1to8', 'sell1to9', 'sellslpoints', 'lot_size', 'day', 'month', 'nifty_open', 'nifty_prev_close', 'nifty_trend', 'trade_time','p&l']
			column_option = st.multiselect("Select main column first", options)
			
			if column_option:
				first_col = column_option[0]
				second_col = column_option[1]

				st.table(pd.crosstab(stock_df[first_col],stock_df[second_col],normalize = 'columns')*100)
				
				plot_type = st.selectbox("select chart type",['Heatmap','Stacked Bar chart','Tree map'])
				if plot_type == 'Heatmap':
					heatmap = sns.heatmap(pd.crosstab(stock_df[first_col],stock_df[second_col],normalize = 'columns')*100)
					st.pyplot(heatmap.figure)

				elif plot_type == 'Stacked Bar chart':
					st.subheader("Coming Soon")

				else:
					st.subheader("Coming Soon")

		

		elif relation_type == 'Categorical - Numerical':
			options = ['buyprice', 'date', 'buytime', 'sl', 'type', 'stock', 'buyslpoints', 'tgt', 'buy1to1', 'buy1to2', 'buy1to3', 'buy1to4', 'buy1to5', 'buy1to6', 'buy1to7', 'buy1to8', 'buy1to9', 'sellprice', 'selltime', 'profit_or_loss', 'remarks', 'trail', 'sell1to1', 'sell1to2', 'sell1to3', 'sell1to4', 'sell1to5', 'sell1to6', 'sell1to7', 'sell1to8', 'sell1to9', 'sellslpoints', 'lot_size', 'day', 'month', 'nifty_open', 'nifty_prev_close', 'nifty_trend', 'trade_time', 'p&l']
			column_option = st.multiselect("Select main column first", options)

			if len(column_option) == 2:
				first_col = column_option[0]
				second_col = column_option[1]
				
				fig, ax = plt.subplots()
				
				stock_df.loc[stock_df[first_col] == stock_df[first_col].value_counts().index[1], second_col].plot(kind='kde', label='Profit', ax=ax)
				stock_df.loc[stock_df[first_col] == stock_df[first_col].value_counts().index[0], second_col].plot(kind='kde', label='Loss', ax=ax)
				
				ax.set_xlabel('Value')
				ax.set_ylabel('Density')
				ax.set_title('Density Plot')
				plt.legend()
				st.pyplot(fig)


	else:
		option = st.selectbox("Select Co-relation Type",['All Columns','Specific Column', 'Pair Plot'])
		if option == "All Columns":
			st.title("Co-relation with other columns")
			st.table(stock_df.corr())

			st.write('## Correlation Heatmap')
			fig, ax = plt.subplots()
			sns.heatmap(stock_df.corr(), annot=True, cmap='coolwarm', ax=ax)
			st.pyplot(fig)

		elif option == 'Specific Column':
			options = ['buyprice', 'date', 'buytime', 'sl', 'type', 'stock', 'buyslpoints', 'tgt', 'buy1to1', 'buy1to2', 'buy1to3', 'buy1to4', 'buy1to5', 'buy1to6', 'buy1to7', 'buy1to8', 'buy1to9', 'sellprice', 'selltime', 'profit_or_loss', 'remarks', 'trail', 'sell1to1', 'sell1to2', 'sell1to3', 'sell1to4', 'sell1to5', 'sell1to6', 'sell1to7', 'sell1to8', 'sell1to9', 'sellslpoints', 'lot_size', 'day', 'month', 'nifty_open', 'nifty_prev_close', 'nifty_trend', 'trade_time', 'p&l']
			column_option = st.selectbox("Select Column", options)
			st.table(stock_df.corr()[str(column_option)])

		else:
			st.write('## Pair Plot')
			fig = sns.pairplot(stock_df)
			fig.savefig('pairplot.png')
			img = Image.open('pairplot.png')
			img_resized = img.resize((800, 800))
			st.image(img_resized)
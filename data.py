import pandas as pd

johns_hopkins_df = pd.read_csv("resources/3_cases_and_deaths_by_state_timeseries.csv")

johns_hopkins_df.to_html("data.html" index = False)

johns_hopkins_table = johns_hopkins_df.to_html()

print(johns_hopkins_table)
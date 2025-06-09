import pandas as pd
from site_scrapper_trial import get_info_case

info = get_info_case('https://casehug.com/cases/bombix')
case_info = [['type', 'skin_name', 'price', 'chance']]
for case in info:
    weapon_type = case.select_one('[data-testid="case-content-card-grid-item-name"]')
    skin_name = case.select_one('[data-testid="case-content-card-grid-item-category"]')
    price = case.select_one('[data-testid="case-content-card-grid-item-single-price"]')
    chance = case.select_one('[data-testid="case-content-card-grid-item-odds-percentage"]') 
    case_info.append([weapon_type.text.strip(), skin_name.text.strip(), float(price.text.strip('$')), float(chance.text.strip('%'))/100])
case_info=pd.DataFrame(case_info)
case_info.columns = case_info.iloc[0]
case_info = case_info[1:].reset_index(drop=True)
case_info['earning'] = case_info['price'] * case_info['chance']
print(case_info['earning'].sum())
case_info.to_excel('tanunahui.xlsx')
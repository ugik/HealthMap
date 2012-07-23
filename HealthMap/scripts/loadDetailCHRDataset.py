from HealthMap.models import Region, Dataset, Datarow, Category, Range
from xlrd import open_workbook,cellname

def run():

#    region = ["Washingtom", "Oregon", "California"]   
#    region_name = "Pacific Coast"

#    region = ["Nevada", "Idaho", "Utah", "Colorado", "Wyoming", "Montana"]   
#    region_name = "Mountain"

#    region = ["Arizona", "New Mexico", "Texas", "Oklahoma"]   
#    region_name = "Southwest"

#    region = ["North Dakota", "South Dakota", "Nebraska", "Kansas", "Minnesota", "Iowa", "Missouri"]   
#    region_name = "Heartland"

#    region = ["Arkansas", "Louisiana", "Mississippi", "Alabama", "Georgia", "Florida", "South Carolina"]   
#    region_name = "Southeast"

#    region = ["Tennessee", "North Carolina", "Kentucky", "West Virginia", "Virginia"]   
#    region_name = "Appalachian Highlands"

#    region = ["Wisconsin", "Illinois", "Indiana", "Ohio", "Michigan"]   
#    region_name = "Midwest"

#    region = ["New York", "New Jersey", "Delaware", "Maryland", "District of Columbia"]   
#    region_name = "Mid-Atlantic"

#    region = ["Connecticut", "Rhode Island", "Massachusetts", "Vermont", "New Hampshire", "Maine"]   
#    region_name = "New England"

#    region = ["Alaska"]   
#    region_name = "Alaska"

#    region = ["Hawaii"]   
#    region_name = "Hawaii"

    region = ["Alaska"]   
    region_name = "Alaska"

    col = [None] * 60
    cat = [None] * 60
    col[0] = "FIPS"
    col[1] = "State"
    col[2] = "County"

    col[3] = "Years of Potential Life Lost Rate : "
    cat[3] = "Health"
    desc[3] = "Age-adjusted years of potential life lost rate per 100,000"

    col[4] = "Fair/Poor Health : "
    cat[4] = "Health"
    desc[4] = "Percent of adults that report fair or poor health (age-adjusted)"

    col[5] = "Physically Unhealthy Days : "
    cat[5] = "Health"
    desc[5] = "Average number of reported physically unhealthy days per month"
    
    col[6] = "Mentally Unhealthy Days : "
    cat[6] = "Health"
    desc[6] = "Average number of reported mentally unhealthy days per month"
    
    col[7] = "Low Birth Weight : "
    cat[7] = "Health"
    desc[7] = "Percent of births with low birth weight (<2,500g)"
    
    col[8] = "Smoking : "
    cat[8] = "Health"
    desc[8] = "Percent of adults that reported currently smoking"
    
    col[9] = "Obesity : "
    cat[9] = "Health"
    desc[9] = "Percent of adults that report BMI >= 30"
    
    col[10] = "Physically Inactive : "
    cat[10] = "Health"
    desc[10] = "Percent of adults that report no leisure time physical activity"
    
    col[11] = "Excessive Drinking : "
    cat[11] = "Health"
    desc[11] = "Percent of adults that report excessive drinking"
    
    col[12] = "Motor Vehicle Mortality Rate : "
    cat[12] = "Safety"
    desc[12] = "Crude motor-vehicle related mortality rate per 100,000 population"
    
    col[13] = "Sexually Transmitted Infections : "
    cat[13] = "Health"
    desc[13] = "Number of chlamydia cases"
    
    col[14] = "Teen Birth Rate : "
    cat[14] = "Health"
    desc[14] = "Teen birth count, ages 15-19"
    
    col[15] = "Uninsured under 65 : "
    cat[15] = "Economic"
    desc[15] = "Total number of people under age 65 without insurance"
    
    col[17] = "Primary Care Physicians : "
    cat[17] = "Environment"
    desc[17] = "Number of primary care physicians in patient care"
    
    col[18] = "ACSC Medicare Preventable Hospital Stays : "
    cat[18] = "Health"
    desc[18] = "Discharges for ambulatory care sensitive conditions/Medicare enrollees"
    
    col[19] = "Medicare Enrollees Diabetic Screening : "
    cat[19] = "Health"
    desc[19] = "Percent of Diabetic Medicare enrollees receiving HbA1c test"
    
    col[20] = "Medicare Enrollees Mammography Screening : "
    cat[20] = "Health"
    desc[20] = "Percent of female Medicare enrollees having at least 1 mammogram in 2 yrs (age 67-69)"
    
    col[21] = "AFGR High School Graduation Rates : "
    cat[21] = "Environment"
    desc[21] = "Calculated average freshman graduation rate"
    
    col[22] = "PSED Post-Secondary Education : "
    cat[22] = "Environment"
    desc[22] = "Adults age 25-44 with some post-secondary education"
    
    col[23] = "Unemployed : "
    cat[23] = "Economic"
    desc[23] = "Number of people age 16+ unemployed and looking for work"
    
    col[24] = "Child Poverty : "
    cat[24] = "Economic"
    desc[24] = "Percent of children (under age 18) living in poverty"
    
    col[25] = "Social-Emotional Support Inadequate : "
    cat[25] = "Health"
    desc[25] = "Percent of adults that report not getting social/emotional support"
    
    col[26] = "Single Parent Households : "
    cat[26] = "Health"
    desc[26] = "Number of children that live in single parent households"
    
    col[27] = "Violent Crime Rate : "
    cat[27] = "Environment"
    desc[27] = "Sum of violent crimes"
    
    col[28] = "Air Pollution Particular Matter Days : "
    cat[28] = "Environment"
    desc[28] = "Number of days that air quality was unhealthy due to fine particulate matter"
    
    col[29] = "Air Pollution Ozone Unhealthy Days : "
    cat[29] = "Environment"
    desc[29] = "Number of days that air quality was unhealthy due to ozone"
    
    col[30] = "Recreational Facilities Access : "
    cat[30] = "Environment"
    desc[30] = "Total recreational facilities"
    
    col[31] = "Health Foods Limited Access : "
    cat[31] = "Environment"
    desc[31] = "Total number of people with limited access to health foods"
    
    col[32] = "Fast Food Restaurants : "
    cat[32] = "Environment"
    desc[32] = "Number of zip codes with a healthy food outlet"


# category: Demographics
    col[33] = "<18 Population <18 : "
    cat[33] = "Demographic"
    desc[33] = ""

    col[34] = "65+ Population : "
    cat[34] = "Demographic"
    desc[34] = ""

    col[35] = "African American Population : "
    cat[35] = "Demographic"
    desc[35] = ""

    col[36] = "American Indian/Alaskan Native Population : "
    cat[36] = "Demographic"
    desc[36] = ""

    col[37] = "Asian Population : "
    cat[37] = "Demographic"
    desc[37] = ""

    col[38] = "Native Hawaiian/Other Pacific Population : "
    cat[38] = "Demographic"
    desc[38] = ""

    col[39] = "Hispanic Population : "
    cat[39] = "Demographic"
    desc[39] = ""

    col[40] = "Not Proficient in English : "
    cat[40] = "Demographic"
    desc[40] = ""

    col[41] = "Female Population : "
    cat[41] = "Demographic"
    desc[41] = ""

    col[42] = "Rural Population : "
    cat[42] = "Demographic"
    desc[42] = ""

    col[43] = "Diabetics : "
    cat[43] = "Demographic"
    desc[43] = ""

    col[44] = "HIV Cases : "
    cat[44] = "Demographic"
    desc[44] = "Total number of HIV cases"

    col[46] = "Primary Care Physicians Ratio : "
    cat[46] = "Demographic"
    desc[46] = "Number of people per PCP"

    col[47] = "Uninsured Adults : "
    cat[47] = "Demographic"
    desc[47] = ""

    col[48] = "Could Not Access Physician Due to Cost : "
    cat[48] = "Demographic"
    desc[48] = ""

    col[50] = "Dentist Ratio : "
    cat[50] = "Demographic"
    desc[50] = "Number of people per dentist"

    col[51] = "Household Income : "
    cat[51] = "Demographic"
    desc[51] = "Median household imcome"

    col[52] = "High Housing Costs : "
    cat[52] = "Demographic"
    desc[52] = ""

    col[53] = "Illiteracy : "
    cat[53] = "Demographic"
    desc[53] = ""

    col[54] = "Homicides : "
    cat[54] = "Demographic"
    desc[54] = "Total number of homicides"

    col[55] = "Access to Health Foods : "
    cat[55] = "Demographic"
    desc[55] = "Percent of zip codes with healthy food outlets"

    print "Loading CHR Detailed Datasets"
        
    hidden_cols = [0, 1, 2, 16, 45, 49]
    book = open_workbook('HealthMap/scripts/data.xls')
    sheet = book.sheet_by_index(1)
    
    # delete existing Datasets
    dat = Dataset.objects.filter(name__in=col)
    if dat:
        dat.delete()
    
    for row_index in range(sheet.nrows):
        state = sheet.cell(row_index,1).value
        fips = sheet.cell(row_index,0).value
        county = sheet.cell(row_index,2).value
        if len(state)>1 and len(county)<1:      # state data row
            print state
                
        elif state in region:
            print ("Processing %s" % state)
            for col_index in range(sheet.ncols):
                if col_index not in hidden_cols:
                    # find Region
                    reg = Region.objects.filter(stateName=state.strip(), fips=fips)
                    proceed = True
                    if not reg:
                        print("Missing State: %s  County:%s" % (state, county))
                        proceed = False
                    # create Dataset
                    cate = Category.objects.filter(name=cat[col_index])
                    if not cate:
                        print("Missing Category: %s" % cat[col_index])
                        proceed = False

                    dataset_name=col[col_index]+region_name
                    
                    if proceed:
                        if not Dataset.objects.filter(name=dataset_name):
                            print("Creating Dataset: %s" % dataset_name)
                            
                            dat = Dataset(category=cate[0], name=dataset_name, description=desc[col_index])
                            dat.save()            
                        dat = Dataset.objects.filter(name=dataset_name)
                        val = sheet.cell(row_index,col_index).value
                        print("data for Region:%s/%s, (%s) Dataset:%s" % (reg[0].state, reg[0].county, str(val).strip(), dataset_name))
                        row = Datarow.objects.filter(dataset=dat[0], region=reg[0])
                        if row:     # cleanup if necessary
                            row.delete()
                        # create Datarow if there is value
                        if len(str(val).strip())>0:
                            row = Datarow(dataset=dat[0], region=reg[0], value=val)
                            row.save()
















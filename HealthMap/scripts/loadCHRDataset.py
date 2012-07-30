from HealthMap.models import Region, Dataset, Datarow, Category, Range
from xlrd import open_workbook,cellname

def run():

    col = [None] * 60
    cat = [None] * 60
    desc = [None] * 60
    source = [None] * 60

    col[0] = "FIPS"
    col[1] = "State"
    col[2] = "County"

    col[3] = "Years of Potential Life Lost Rate"
    cat[3] = "Health"
    desc[3] = "Age-adjusted years of potential life lost rate per 100,000"
    source[3] = "National Center for Health Statistics (NCHS) 2006-2008"
    
    col[4] = "Fair/Poor Health"
    cat[4] = "Health"
    desc[4] = "Percent of adults that report fair or poor health (age-adjusted)"
    source[4] = "Behavioral Risk Factor Surveillance System (BRFSS) 2004-2010"

    col[5] = "Physically Unhealthy Days"
    cat[5] = "Health"
    desc[5] = "Average number of reported physically unhealthy days per month"
    source[5] = "Behavioral Risk Factor Surveillance System (BRFSS) 2004-2010"

    col[6] = "Mentally Unhealthy Days"
    cat[6] = "Health"
    desc[6] = "Average number of reported mentally unhealthy days per month"
    source[6] = "Behavioral Risk Factor Surveillance System (BRFSS) 2004-2010"
    
    col[7] = "Low Birth Weight"
    cat[7] = "Health"
    desc[7] = "Percent of births with low birth weight (<2,500g)"
    source[7] = "Vital Statistics, National Center for Health Statistics (NCHS) 2002-2008"

    col[8] = "Smoking"
    cat[8] = "Health"
    desc[8] = "Percent of adults that reported currently smoking"
    source[8] = "Behavioral Risk Factor Surveillance System (BRFSS) 2004-2010"
    
    col[9] = "Obesity"
    cat[9] = "Health"
    desc[9] = "Percent of adults that report BMI >= 30"
    source[9] = "National Center for Chronic Disease Prevention and Health 2009"
  
    col[10] = "Physically Inactive"
    cat[10] = "Health"
    desc[10] = "Percent of adults that report no leisure time physical activity"
    source[10] = "National Center for Chronic Disease Prevention and Health 2009"
    
    col[11] = "Excessive Drinking"
    cat[11] = "Health"
    desc[11] = "Percent of adults that report excessive drinking"
    source[11] = "Behavioral Risk Factor Surveillance System (BRFSS) 2004-2010"
    
    col[12] = "Motor Vehicle Mortality Rate"
    cat[12] = "Safety"
    desc[12] = "Crude motor-vehicle related mortality rate per 100,000 population"
    source[12] = "Vital Statistics, National Center for Health Statistics (NCHS) 2002-2008"
    
    col[13] = "Sexually Transmitted Infections"
    cat[13] = "Health"
    desc[13] = "Number of chlamydia cases"
    source[13] = "CDC National Center for Hepatitis, HIV, STD 2009"
    
    col[14] = "Teen Birth Rate"
    cat[14] = "Health"
    desc[14] = "Teen birth count, ages 15-19"
    source[14] = "Vital Statistics, National Center for Health Statistics (NCHS) 2002-2008"
    
    col[15] = "Uninsured under 65"
    cat[15] = "Economic"
    desc[15] = "Total number of people under age 65 without insurance"
    source[15] = "Census/American Community Survey (ACS) 2009"
    
    col[17] = "Primary Care Physicians"
    cat[17] = "Environment"
    desc[17] = "Number of primary care physicians in patient care"
    source[17] = "Health Resources and Services Administration 2009"
    
    col[18] = "ACSC Medicare Preventable Hospital Stays"
    cat[18] = "Health"
    desc[18] = "Discharges for ambulatory care sensitive conditions/Medicare enrollees"
    source[18] = "Dartmouth Atlas 2009"
    
    col[19] = "Medicare Enrollees Diabetic Screening"
    cat[19] = "Health"
    desc[19] = "Percent of Diabetic Medicare enrollees receiving HbA1c test"
    source[19] = "Dartmouth Atlas 2009"
    
    col[20] = "Medicare Enrollees Mammography Screening"
    cat[20] = "Health"
    desc[20] = "Percent of female Medicare enrollees having at least 1 mammogram in 2 yrs (age 67-69)"
    source[20] = "Dartmouth Atlas 2009"
    
    col[21] = "AFGR High School Graduation Rates"
    cat[21] = "Environment"
    desc[21] = "Calculated average freshman graduation rate"
    source[21] = "Sate sources"
    
    col[22] = "PSED Post-Secondary Education"
    cat[22] = "Environment"
    desc[22] = "Adults age 25-44 with some post-secondary education"
    source[22] = "Census/American Community Survey (ACS) 2006-2010"
    
    col[23] = "Unemployed"
    cat[23] = "Economic"
    desc[23] = "Number of people age 16+ unemployed and looking for work"
    source[23] = "Unemployment Statistics, Bureau of Labor Statistics 2010"
    
    col[24] = "Child Poverty"
    cat[24] = "Economic"
    desc[24] = "Percent of children (under age 18) living in poverty"
    source[24] = "Census/CPS 2010"
    
    col[25] = "Social-Emotional Support Inadequate"
    cat[25] = "Health"
    desc[25] = "Percent of adults that report not getting social/emotional support"
    source[25] = "Behavioral Risk Factor Surveillance System (BRFSS) 2004-2010"
    
    col[26] = "Single Parent Households"
    cat[26] = "Health"
    desc[26] = "Number of children that live in single parent households"
    source[26] = "Census/American Community Survey (ACS) 2006-2010"
    
    col[27] = "Violent Crime Rate"
    cat[27] = "Environment"
    desc[27] = "Sum of violent crimes"
    source[27] = "Federal Bureau of Investigation 2007-2009"
    
    col[28] = "Air Pollution Particular Matter Days"
    cat[28] = "Environment"
    desc[28] = "Number of days that air quality was unhealthy due to fine particulate matter"
    source[28] = "CDC Environmental Protection Agency (EPA) 2007"
    
    col[29] = "Air Pollution Ozone Unhealthy Days"
    cat[29] = "Environment"
    desc[29] = "Number of days that air quality was unhealthy due to ozone"
    source[29] = "CDC Environmental Protection Agency (EPA) 2007"
    
    col[30] = "Recreational Facilities Access"
    cat[30] = "Environment"
    desc[30] = "Total recreational facilities"
    source[30] = "Census County Business Patterns 2009"
    
    col[31] = "Health Foods Limited Access"
    cat[31] = "Environment"
    desc[31] = "Total number of people with limited access to health foods"
    source[31] = "Census Zip Code Business Patterns 2009"
    
    col[32] = "Fast Food Restaurants"
    cat[32] = "Environment"
    desc[32] = "Number of zip codes with a healthy food outlet"
    source[32] = "Census County Business Patterns 2009"


# category: Demographics
    col[33] = "<18 Population"
    cat[33] = "Demographic"
    desc[33] = "Percent"
    source[33] = "US Census Bureau 2009"

    col[34] = "65+ Population"
    cat[34] = "Demographic"
    desc[34] = "Percent"
    source[34] = "US Census Bureau 2009"

    col[35] = "African American Population"
    cat[35] = "Demographic"
    desc[35] = "Percent"
    source[35] = "US Census Bureau 2009"

    col[36] = "American Indian/Alaskan Native Population"
    cat[36] = "Demographic"
    desc[36] = "Percent"
    source[36] = "US Census Bureau 2009"

    col[37] = "Asian Population"
    cat[37] = "Demographic"
    desc[37] = "Percent"
    source[37] = "US Census Bureau 2009"

    col[38] = "Native Hawaiian/Other Pacific Population"
    cat[38] = "Demographic"
    desc[38] = "Percent"
    source[38] = "US Census Bureau 2009"

    col[39] = "Hispanic Population"
    cat[39] = "Demographic"
    desc[39] = "Percent"
    source[39] = "US Census Bureau 2009"

    col[40] = "Not Proficient in English"
    cat[40] = "Demographic"
    desc[40] = "Percent"
    source[40] = "US Census Bureau 2009"

    col[41] = "Female Population"
    cat[41] = "Demographic"
    desc[41] = "Percent"
    source[41] = "US Census Bureau 2009"

    col[42] = "Rural Population"
    cat[42] = "Demographic"
    desc[42] = "Percent"
    source[42] = "US Census Bureau 2009"

    col[43] = "Diabetics"
    cat[43] = "Demographic"
    desc[43] = "Percent"
    source[43] = "Centers for Disease Control (CDC) 2009"

    col[44] = "HIV Cases"
    cat[44] = "Demographic"
    desc[44] = "Rate of HIV cases"
    source[44] = "National Center for Hepatitis, HIC, STD 20008"

    col[46] = "Primary Care Physicians Ratio"
    cat[46] = "Demographic"
    desc[46] = "Number of people per PCP"
    source[46] = "Health Resources & Services Administration (HRSA) 2007"

    col[47] = "Uninsured Adults"
    cat[47] = "Demographic"
    desc[47] = "Percent"
    source[47] = "Small Area Health Insurance Estimates (SAHIE 2009"

    col[48] = "Could Not Access Physician Due to Cost"
    cat[48] = "Demographic"
    desc[48] = "Percent"
    source[48] = "Behavioral Risk Factor Surveillance System (BRFSS) 2004-2010"

    col[50] = "Dentist Ratio"
    cat[50] = "Demographic"
    desc[50] = "Number of people per dentist"
    source[50] = "Health Resources & Services Administration (HRSA) 2007"

    col[51] = "Household Income"
    cat[51] = "Demographic"
    desc[51] = "Median household imcome"
    source[51] = "Small Area Health Insurance Estimates (SAHIE 2009"

    col[52] = "High Housing Costs"
    cat[52] = "Demographic"
    desc[52] = "Percent"
    source[52] = "ACS Estimates 2006"

    col[53] = "Illiteracy"
    cat[53] = "Demographic"
    desc[53] = "Percent"
    source[53] = "National Center for Education Statistics 2003"

    col[54] = "Homicides"
    cat[54] = "Demographic"
    desc[54] = "Total number of homicides"
    source[54] = "National Center for Health Statistics 2002-2008"

    col[55] = "Access to Health Foods"
    cat[55] = "Demographic"
    desc[55] = "Percent of zip codes with healthy food outlets"
    source[55] = "Census Zip Code Business Patterns 2009"


    # clean up if necessary
    cate = Category.objects.filter(name__in=['Health','Safety','Environment','Economic','Demographic'])
    if cate:
        cate.delete()
    # create the Categories
    cate = Category(name="Health")
    cate.save()
    cate = Category(name="Safety")
    cate.save()
    cate = Category(name="Environment")
    cate.save()
    cate = Category(name="Economic")
    cate.save()
    cate = Category(name="Demographic")
    cate.save()
    print "Created Categories"

    print "Loading CHR Datasets"
        
    hidden_cols = [0, 1, 2, 16, 45, 49]
    book = open_workbook('HealthMap/scripts/data.xls')
    sheet = book.sheet_by_index(1)
    
    # delete existing Datasets
    dat = Dataset.objects.filter(name__in=col)
    if dat:
        dat.delete()
    
    for row_index in range(sheet.nrows):
        state = sheet.cell(row_index,1).value
        county = sheet.cell(row_index,2).value
        if len(state)>1 and len(county)<1:      # state data row
#            print state

            for col_index in range(sheet.ncols):
                if col_index not in hidden_cols:
                    # find Region
                    reg = Region.objects.filter(stateName=state.strip())
                    if not reg:
                        print("Missing State: %s" % state)
                    # create Dataset
                    cate = Category.objects.filter(name=cat[col_index])
                    if not cate:
                        print("Missing Category: %s" % cat[col_index])
                    if not Dataset.objects.filter(name=col[col_index]):
                        print("Creating Dataset: %s" % col[col_index])
                        dat = Dataset(category=cate[0], 
                                              name=col[col_index], 
                                              description=desc[col_index], 
                                              citations=source[col_index])
                        dat.save()            
                    dat = Dataset.objects.filter(name=col[col_index])
                    val = sheet.cell(row_index,col_index).value
                    print("data for Region:%s, [%s] (%s) Dataset:%s" % (reg[0].state, col_index, str(val).strip(), col[col_index]))
                    # create Datarow if there is value
                    if len(str(val).strip())>0:
                        row = Datarow(dataset=dat[0], region=reg[0], value=val)
                        row.save()
















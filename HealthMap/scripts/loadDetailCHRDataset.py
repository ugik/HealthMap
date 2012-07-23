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
#    region_latitude = "36.597889"
#    region_longitude = "-83.166504"
#    region_zoom = "6"

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

    region = []   
    region_name = "Appalachian Highlands"

    col = [None] * 60
    cat = [None] * 60
    col[0] = "FIPS"
    col[1] = "State"
    col[2] = "County"

    col[3] = "Years of Potential Life Lost Rate : "
    cat[3] = "Health"

    col[4] = "Fair/Poor Health : "
    cat[4] = "Health"

    col[5] = "Physically Unhealthy Days : "
    cat[5] = "Health"
    
    col[6] = "Mentally Unhealthy Days : "
    cat[6] = "Health"
    
    col[7] = "Low Birth Weight : "
    cat[7] = "Health"
    
    col[8] = "Smoking : "
    cat[8] = "Health"
    
    col[9] = "Obesity : "
    cat[9] = "Health"
    
    col[10] = "Physically Inactive : "
    cat[10] = "Health"
    
    col[11] = "Excessive Drinking : "
    cat[11] = "Health"
    
    col[12] = "Motor Vehicle Mortality Rate : "
    cat[12] = "Safety"
    
    col[13] = "Sexually Transmitted Infections : "
    cat[13] = "Health"
    
    col[14] = "Teen Birth Rate : "
    cat[14] = "Health"
    
    col[15] = "Uninsured under 65 : "
    cat[15] = "Economic"
    
    col[17] = "Primary Care Physicians : "
    cat[17] = "Environment"
    
    col[18] = "ACSC Medicare Preventable Hospital Stays : "
    cat[18] = "Health"
    
    col[19] = "Medicare Enrollees Diabetic Screening : "
    cat[19] = "Health"
    
    col[20] = "Medicare Enrollees Mammography Screening : "
    cat[20] = "Health"
    
    col[21] = "AFGR High School Graduation Rates : "
    cat[21] = "Environment"
    
    col[22] = "PSED Post-Secondary Education : "
    cat[22] = "Environment"
    
    col[23] = "Unemployed : "
    cat[23] = "Economic"
    
    col[24] = "Child Poverty : "
    cat[24] = "Economic"
    
    col[25] = "Social-Emotional Support Inadequate : "
    cat[25] = "Health"
    
    col[26] = "Single Parent Households : "
    cat[26] = "Health"
    
    col[27] = "Violent Crime Rate : "
    cat[27] = "Environment"
    
    col[28] = "Air Pollution Particular Matter Days : "
    cat[28] = "Environment"
    
    col[29] = "Air Pollution Ozone Unhealthy Days : "
    cat[29] = "Environment"
    
    col[30] = "Recreational Facilities Access : "
    cat[30] = "Environment"
    
    col[31] = "Health Foods Limited Access : "
    cat[31] = "Environment"
    
    col[32] = "Fast Food Restaurants : "
    cat[32] = "Environment"


# category: Demographics
    col[33] = "<18 Population <18 : "
    cat[33] = "Demographic"

    col[34] = "65+ Population : "
    cat[34] = "Demographic"

    col[35] = "African American Population : "
    cat[35] = "Demographic"

    col[36] = "American Indian/Alaskan Native Population : "
    cat[36] = "Demographic"

    col[37] = "Asian Population : "
    cat[37] = "Demographic"

    col[38] = "Native Hawaiian/Other Pacific Population : "
    cat[38] = "Demographic"

    col[39] = "Hispanic Population : "
    cat[39] = "Demographic"

    col[40] = "Not Proficient in English : "
    cat[40] = "Demographic"

    col[41] = "Female Population : "
    cat[41] = "Demographic"

    col[42] = "Rural Population : "
    cat[42] = "Demographic"

    col[43] = "Diabetics : "
    cat[43] = "Demographic"

    col[44] = "HIV Cases : "
    cat[44] = "Demographic"

    col[46] = "Primary Care Physicians Ratio : "
    cat[46] = "Demographic"

    col[47] = "Uninsured Adults : "
    cat[47] = "Demographic"

    col[48] = "Could Not Access Physician Due to Cost : "
    cat[48] = "Demographic"

    col[50] = "Dentist Ratio : "
    cat[50] = "Demographic"

    col[51] = "Household Income : "
    cat[51] = "Demographic"

    col[52] = "High Housing Costs : "
    cat[52] = "Demographic"

    col[53] = "Illiteracy : "
    cat[53] = "Demographic"

    col[54] = "Homicides : "
    cat[54] = "Demographic"

    col[55] = "Access to Health Foods : "
    cat[55] = "Demographic"

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
                            
                            dat = Dataset(category=cate[0], name=dataset_name, 
                                                  maplatitude=region_latitude, maplongitude=region_longitude, mapzoom=region_zoom)
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
















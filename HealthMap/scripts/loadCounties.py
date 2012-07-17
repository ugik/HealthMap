from HealthMap.models import Region, Dataset, Datarow, Category, Range
from xlrd import open_workbook,cellname

def run():

    # clean up if necessary
    print "Loading County data"

    book = open_workbook('HealthMap/scripts/data.xls')
    sheet = book.sheet_by_index(1)
    
    for row_index in range(sheet.nrows):
        fips = sheet.cell(row_index,0).value
        state = sheet.cell(row_index,1).value
        county = sheet.cell(row_index,2).value
        if len(state)>1 and len(county)<1:      # state data row
            print state
        if len(fips)==5:
            state_reg = Region.objects.filter(stateName=state.strip())
            state_abbrev = state_reg[0].state    # get State abbrev
            reg = Region.objects.filter(state=state_abbrev, county=county)
            if reg:
               reg.delete()     # cleanup existing
            print("[%s] %s, County: %s (%s)" % (state_abbrev, state, county, fips))
            reg = Region(state=state_abbrev, stateName=state, county=county, fips=fips)
            reg.save()


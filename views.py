from flask import render_template, request
from app import app
from schedule_api import *

@app.route('/')
def main():

    return render_template('main.html')

@app.route('/about/')
def about():

    return render_template('about.html')

@app.route('/about/index/')
def index():
    options = {}

    options['terms'] = get_terms()

    return render_template('index.html', **options)


@app.route('/about/index/browse/<TermCode>/')
def show_school_name(TermCode):
	#show the user all the school names
	options = {}

	options['TermCode'] = TermCode
	options['SchoolList'] = get_schools(TermCode)

	return render_template('show_school_name.html', **options)


@app.route ('/about/index/browse/<TermCode>/school/<SchoolCode>/')
def show_subject_choices(TermCode, SchoolCode):
	#show the user all the subject choices
	options = {}

	options['TermCode'] = TermCode
	options['SchoolCode'] = SchoolCode
	options['SubjectList'] = get_subjects(TermCode, SchoolCode)

	return render_template('show_subject_choices.html', **options)

@app.route ('/about/index/browse/<TermCode>/school/<SchoolCode>/subject/<SubjectCode>')
def show_catalog_numbers(TermCode, SchoolCode, SubjectCode):
	#show the user all the catalog numbers
	options = {}

	options['TermCode'] = TermCode
	options['SchoolCode'] = SchoolCode
	options['SubjectCode'] = SubjectCode
	options['SubjectList'] = get_subjects(TermCode, SchoolCode)
	options['CatalogList'] = get_catalog_numbers(TermCode, SchoolCode, SubjectCode)

	return render_template('show_catalog_numbers.html', **options)

@app.route ('/about/index/browse/<TermCode>/school/<SchoolCode>/subject/<SubjectCode>/catalog/<CatalogNumber>/coursedescri')
def show_course_description(TermCode, SchoolCode, SubjectCode, CatalogNumber):
	#show the user all the course description
	options = {}

	options['TermCode'] = TermCode
	options['SchoolCode'] = SchoolCode
	options['SubjectCode'] = SubjectCode
	options['CatalogNumber'] = CatalogNumber
	options['CourseList'] = get_course_description(TermCode, SchoolCode, SubjectCode, CatalogNumber)
	options['SectionNumList'] = get_section_nums(TermCode, SchoolCode, SubjectCode, CatalogNumber)

	# array for section details
	DetailsArray = []

	# array for meeting times
	MeetingArray = []

	# loop through options['SectionNumList'], make calls to get_meetings and get_details
	for i in options['SectionNumList']:
		DetailsArray.append(get_section_details(TermCode, SchoolCode, SubjectCode, CatalogNumber, i))
	for i in options['SectionNumList']:
	    MeetingArray.append(get_meetings(TermCode, SchoolCode, SubjectCode, CatalogNumber, i))

	options['SectionDetailsList'] = DetailsArray
	options['MeetingList'] = MeetingArray
	# get_meetings, get_section_details
	return render_template('show_course_description.html', **options)


@app.route ('/about/index/browse/<TermCode>/school/<SchoolCode>/subject/<SubjectCode>/catalog/<CatalogNumber>/section')
def show_section_nums(TermCode, SchoolCode, SubjectCode, CatalogNumber):
	#show the user all the section numbers
	options = {}

	options['TermCode'] = TermCode
	options['SchoolCode'] = SchoolCode
	options['SubjectCode'] = SubjectCode
	options['CatalogNumber'] = CatalogNumber
	options['SectionNumList'] = get_section_nums(TermCode, SchoolCode, SubjectCode, CatalogNumber)

	return render_template('show_course_description.html', **options)

@app.route ('/about/index/browse/<TermCode>/school/<SchoolCode>/subject/<SubjectCode>/catalog/<CatalogNumber>/section/<SectionNumber>/secdetails')
def show_section_details(TermCode, SchoolCode, SubjectCode, CatalogNumber, SectionNumber):
	#show the user all the section details
	options = {}
	options['TermCode'] = TermCode
	options['SchoolCode'] = SchoolCode
	options['SubjectCode'] = SubjectCode
	options['CatalogNumber'] = CatalogNumber
	options['SectionNumber'] = SectionNumber
	options['SectionDetailsList'] = get_section_details(TermCode, SchoolCode, SubjectCode, CatalogNumber, SectionNumber)

	return render_template('show_course_description.html', **options)


@app.route ('/about/index/browse/<TermCode>/school/<SchoolCode>/subject/<SubjectCode>/catalog/<CatalogNumber>/section/<SectionNumber>/meeting')
def show_meetings(TermCode, SchoolCode, SubjectCode, CatalogNumber, SectionNumber):
	#show the user all the meetings
	options = {}

	options['TermCode'] = TermCode
	options['SchoolCode'] = SchoolCode
	options['SubjectCode'] = SubjectCode
	options['CatalogNumber'] = CatalogNumber
	options['SectionNumber'] = SectionNumber
	options['MeetingList'] = get_meetings(TermCode, SchoolCode, SubjectCode, CatalogNumber, SectionNumber)

	return render_template('show_course_description.html', **options)

@app.route ('/about/index/browse/<TermCode>/school/<SchoolCode>/subject/<SubjectCode>/catalog/<CatalogNumber>/section/<SectionNumber>/textbooks')
def show_textbooks(TermCode, SchoolCode, SubjectCode, CatalogNumber, SectionNumber):
	#show the user all the textbooks
	options = {}

	options['TermCode'] = TermCode
	options['SchoolCode'] = SchoolCode
	options['SubjectCode'] = SubjectCode
	options['CatalogNumber'] = CatalogNumber
	options['SectionNumber'] = SectionNumber
	options['TextbooksList'] = get_textbooks(TermCode, SchoolCode, SubjectCode, CatalogNumber, SectionNumber)

	return render_template('show_course_description.html', **options)

	
@app.route ('/about/index/browse/<TermCode>/school/<SchoolCode>/subject/<SubjectCode>/catalog/<CatalogNumber>/section/<SectionNumber>/instructors')
def show_instructors(TermCode, SchoolCode, SubjectCode, CatalogNumber, SectionNumber):
	#show the user all the instructors
	options = {}

	options['TermCode'] = TermCode
	options['SchoolCode'] = SchoolCode
	options['SubjectCode'] = SubjectCode
	options['CatalogNumber'] = CatalogNumber
	options['SectionNumber'] = SectionNumber
	options['InstructorsList'] = get_instructors(TermCode, SchoolCode, SubjectCode, CatalogNumber, SectionNumber)

	return render_template('show_course_description.html', **options)

@app.route ('/about/index/browse/<TermCode>/school/<SchoolCode>/subject/<SubjectCode>/catalog/<CatalogNumber>/coursedescri/map')
def show_map(TermCode, SchoolCode, SubjectCode, CatalogNumber):
	#show the user all the course description
	options = {}

	options['TermCode'] = TermCode
	options['SchoolCode'] = SchoolCode
	options['SubjectCode'] = SubjectCode
	options['CatalogNumber'] = CatalogNumber
	options['CourseList'] = get_course_description(TermCode, SchoolCode, SubjectCode, CatalogNumber)
	options['SectionNumList'] = get_section_nums(TermCode, SchoolCode, SubjectCode, CatalogNumber)

	# array for section details
	DetailsArray = []

	# array for meeting times
	MeetingArray = []

	# loop through options['SectionNumList'], make calls to get_meetings and get_details
	for i in options['SectionNumList']:
		DetailsArray.append(get_section_details(TermCode, SchoolCode, SubjectCode, CatalogNumber, i))
	for i in options['SectionNumList']:
	    MeetingArray.append(get_meetings(TermCode, SchoolCode, SubjectCode, CatalogNumber, i))

	options['SectionDetailsList'] = DetailsArray
	options['MeetingList'] = MeetingArray
	# get_meetings, get_section_details

	
		

	
	
	
	
	return render_template('map.html', **options)






	'''

dct = {'A&AB':'Art & Architecture Building', 'AH': 'Angell Hall', 'AL': 'Walter E. Lay Automotive Lab', 'ALH':'Alice Lloyd Hall', 'ANNEX':'Public Policy Annex, 1015 E. Huron', 
	'ARGUS2':'Argus Building II, Television Center, 408 S. Fourth Street', 'ARGUS3':'Argus Building III, 416 S. Fourth Street','ARR':'Location to be Arranged', 'BAM HALL' :'Blanch Anderson Moore Hall, School of Music'	,
'BELL POOL'	:'Margaret Bell Pool, Central Campus Recreation Building'	,'BEYST' :	'Bob and Betty Beyster Building (formerly CSE)'	,'BIOL STAT'	:'Biological Station'	,'BMT'	:'Burton Memorial Tower',	
'BOT GARD'	:'Matthaei Botanical Gardens, Dixboro Road'	,'BSRB'	:'Biomedical Science Research Building'	,'BURS'	:'Bursley Hall'	,'BUS'	:'Business Administration',	'CAMP DAVIS'	:'Camp Davis'	,'CCL'	:'Clarence Cook Little Building',	
'CCRB'	:'Central Campus Recreation Building'	'CHEM'	:'Chemistry Building'	,'CHRYS'	:'Chrysler Center',	'COMM PARK'	:'Commerce Park'	,'COOL'	:'Cooley Building',	'COUZENS'	:'Couzens Hall',	'CPH'	:'Children's Psychiatric Hospital',	
'CRISLER'	:'Crisler Arena',	'CCSB'	:'Campus Safety Services Building, 1239 Kipke Dr.',	'DANA'	:'Dana Building (School of Natural Resources & Environment)'	,
'DANCE'	:'Dance Building, 1310 N University Court','DC'	:'Duderstadt Center	','DENN'	:'David M. Dennison Building (to be renamed Weiser Hall)',	'DENT'	:'Dental Building',	'DOW'	:'Dow Engineering Building'	,'E-BUS'	:'Executive Education',	
'EECS'	:'Electrical Engineering and Computer Science Building',	'EH'	:'East Hall	','EQ'	:'East Quadrangle','ERB1'	:'Engineering Research Building 1'	,'ERB2'	:'Engineering Research Building 2'	,'EWRE'	:'Environmental & Water Resources Engineering Building'	,
'FA CAMP'	:'Fresh Air Camp, Pinckney'	,'FORD LIB'	:'Ford Library	','FXB'	:'Francois-Xavier Bagnoud Building'	,'GFL'	:'Gorguze Family Laboratory (formerly EPB)',	'GGBL'	:'G. G. Brown Laboratory'	,
'GLIBN'	:'Harlan Hatcher Graduate Library, North'	,'HH'	:'Haven Hall'	,'HUTCH'	:'Hutchins Hall,	'IM POOL'	:'Intramural Building',	'IOE'	:'Industrial and Operations Engineering Building'	,'ISR'	:'Institute for Social Research	',
'K-BUS'	:'Kresge Library'	,'KEC'	:'Kellogg Eye Center	,'KEENE THTR EQ'	:'Keene Theater, Residential College, East Quadrangle',	'KELSEY'	:'Kelsey Museum of Archaeology',	'KHRI'	:'Kresge Hearing Research Institute'	,
'LANE'	:'Lane Hall	','LBME'	:'Lurie Biomedical Engineering Building'	,'LEAG'	:'Michigan League','LEC'	:'Lurie Engineering Center',	'LLIB'	:'Law Library',	'LORCH'	:'Lorch Hall'	,
'LSA'	:'Literature, Science, and the Arts Building'	,'LSI'	:'Life Sciences Institute',	'LSSH'	:'Law School South Hall','MARKLEY'	:'Mary Markley Hall',	'MAX KADE'	:'Max Kade House, 627 Oxford Street',	
'MH	:'Mason Hall',	'MHRI'	:'Mental Health Research Institute',	'MLB'	:'Modern Languages Building',	'MONREOCTY HD'	:'Monroe County Health Department','MOSHER'	:'Mosher Jordan Hall'	,
'MOTT'	:'C. S. Mott Children's Hospital'	,'MSC1'	:'Medical Science, Building I',	'MSC2'	:'Medical Science, Building II',	'MSRB3'	:'Medical Science Research, Building III',	'NAME'	:'Naval Architecture and Marine Engineering Building'	,
'NCRB'	:'North Campus Recreation Building',	'NCRC'	:'North Campus Research Complex',	'NIB'	:'300 North Ingalls Building',	'400NI'	:'400 North Ingalls Building (old School of Nursing Building)',	
'NORTHVILLEPH'	:'Northville State Hospital',	'NQ'	:'North Quad	','NS'	:'Edward Henry Kraus Natural Science Building',	'OBL'	:'Observatory Lodge, 1402 Washington Heights',	
'PALM'	:'Palmer Commons	','PHOENIXLAB'	:'Phoenix Memorial Laboratory',	'PIER'	:'Pierpont Commons',	'POWER CTR'	:'Power Center for the Performing Arts',	
'RACK'	:'Horace H. Rackham, School of Graduate Studies',	'RAND'	:'Randall Laboratory'	,'R-BUS'	:'Ross School of Business Building',	'REVELLI'	:'William D. Revelli Hall',	'ROSS AC'	:'Stephen M. Ross Academic Center',	
'RUTHVEN	:'A. G.' Ruthven Museums Building (Natural History Museum)',	'SCHEM'	:'Glenn E. Schembechler Hall'	,'SEB'	:'School of Education Building',	'SHAPIRO'	:'Shapiro Undergraduate Library',	
'SM'	:'Earl V. Moore Building, School of Music',	'SNB'	:'School of Nursing Building	','SPH1'	:'Henry Vaughan Building, School of Public Health I	','SPH2'	:'Thomas Francis, Jr Building, School of Public Health II',	
'SRB'	:'Space Research Building',	'SSWB'	:'School of Social Work Building'	,'STAMPS'	:'Stamps Auditorium	','STB'	:'202 South Thayer Building',	'STJOSEPH HOSP'	:'St. Joseph Mercy Hospital',	
'STOCKWELL'	:'Stockwell Hall',	'STRNS'	:'Sterns Building',	'T&TB'	:'Track & Tennis Building',	'TAP'	:'Tappan Hall'	,'TAUBL'	:'Learning Resource Center, Taubman Medical Library',	'TISCH'	:'Tisch Hall'	,
'UM HOSP'	:'University Hospital',	'UMMA'	:'University of Michigan Museum of Art (Alumni Memorial Hall)',	'UNION'	:'Michigan Union'	,'USB'	:'Undergraduate Science Building'	,'UTOWER'	:'University Towers, 1225 S. University',	
'VETERANSHOSP'	:'Veterans Administration Hospital',	'WASHCTY HD'	:'Washtenaw County Health Department',	'W-BUS'	:'Wyly Hall',	'WDC'	:'Charles R. Walgreen, Jr. Drama Center','WEILL'	:'Joan and Sanford Weill Hall',	
'WEIS'	:'Weiser Hall (formerly Dennsion Building)',	'WH' :'West Hall',	'WOMEN'S HOSP'	:'Women's Hospital'	,'WQ'	:'West Quad }
	'''
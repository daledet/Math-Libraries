import survey_math
import csv

class TieOnSurvey:
    def __init__(self, md, inc, az, tvd, ns, ew, vs,):
        self.md = md
        self.inc = inc
        self.az = az
        self.tvd = tvd
        self.ns = ns
        self.ew = ew
        self.vs = vs
    def __repr__(self):
        return f'{self.md}, {self.inc}, {self.az} , {self.tvd} , {self.ns} , {self.ew} , {self.ew},'

class Survey:
    def __init__(self, md, inc, az,):
        self.md = md
        self.inc = inc
        self.az = az
    def __repr__(self):
        return f'{self.md}, {self.inc}, {self.az}'

class Coordinates:
    def __init__(self, tvd, ns, ew, vs,):
        self.tvd = tvd
        self.ns = ns
        self.ew = ew
        self.vs = vs
    def __repr__(self):
        return f'{self.tvd} , {self.ns} , {self.ew} , {self.vs},'

print('Tie On Survey: ')
tie_on_survey = TieOnSurvey(int(input('MD: ')) , int(input('Inc: ')) , int(input('Az: ')) , int(input('N/S: ')) , int(input('E/W: ')) , int(input('TVD: ')) , int(input('VS: ')) , )

with open('survey_file.csv', 'w') as survey_file:
    writer = csv.writer(survey_file)
    writer.writerow(['Tie on Survey: ', tie_on_survey.md , tie_on_survey.inc , tie_on_survey.az , tie_on_survey.tvd , tie_on_survey.ns , tie_on_survey.ew , tie_on_survey.vs ,])

survey_number = 0
survey_points = []

print('Survey: ')
survey_point = Survey(int(input('MD: ')) , int(input('Inc: ')) , int(input('Az: ')) ,)
print(survey_point)
course_length = survey_point.md - tie_on_survey.md

dls_degrees = survey_math.DlFormDeg(survey_point.inc , tie_on_survey.inc , 1 , survey_point.az , tie_on_survey.az)
dls_radians = survey_math.DlFormRad(survey_point.inc , tie_on_survey.inc , 1 , survey_point.az , tie_on_survey.az)
ratio_factor = survey_math.RatioFactor(2 , dls_radians , dls_degrees)

coordinates = Coordinates((survey_math.TVD(course_length , 2 , tie_on_survey.inc, survey_point.inc , ratio_factor ,) + tie_on_survey.tvd),
(survey_math.NorthSouth(100 , 2 , tie_on_survey.inc , tie_on_survey.az , survey_point.inc , survey_point.az , ratio_factor) + tie_on_survey.ns) ,
(survey_math.EastWest(100 , 2 , tie_on_survey.inc , tie_on_survey.az , survey_point.inc , survey_point.az , ratio_factor) + tie_on_survey.ew) ,
(survey_math.VS(100 , 2 , tie_on_survey.inc ,  survey_point.inc , ratio_factor ,)) + tie_on_survey.vs )

with open('survey_file.csv', 'a') as survey_file:
    writer = csv.writer(survey_file)
    writer.writerow([survey_point.md , survey_point.inc , survey_point.az , coordinates.tvd , coordinates.ns , coordinates.ew , coordinates.vs , ])

survey_points.append({
    'survey_point': survey_point,
    'coordinates': coordinates,
})

while True:
    print('Survey: ')
    survey_point = Survey(int(input('MD: ')) , int(input('Inc: ')) , int(input('Az: ')) ,)
    course_length = survey_point.md - survey_points[-1]['survey_point'].md

    dls_degrees = survey_math.DlFormDeg(survey_point.inc , survey_points[-1]['survey_point'].inc , 1 , survey_point.az , survey_points[-1]['survey_point'].az)
    dls_radians = survey_math.DlFormRad(survey_point.inc , survey_points[-1]['survey_point'].inc , 1 , survey_point.az , survey_points[-1]['survey_point'].az)
    ratio_factor = survey_math.RatioFactor(2 , dls_radians , dls_degrees)

    coordinates = Coordinates((survey_math.TVD(course_length , 2 , survey_points[-1]['survey_point'].inc, survey_point.inc , ratio_factor ,) + survey_points[-1]['coordinates'].tvd),
    (survey_math.NorthSouth(100 , 2 , survey_points[-1]['survey_point'].inc , survey_points[-1]['survey_point'].az , survey_point.inc , survey_point.az , ratio_factor) + survey_points[-1]['coordinates'].ns) ,
    (survey_math.EastWest(100 , 2 , survey_points[-1]['survey_point'].inc , survey_points[-1]['survey_point'].az , survey_point.inc , survey_point.az , ratio_factor) + survey_points[-1]['coordinates'].ew) ,
    (survey_math.VS(100 , 2 , survey_points[-1]['survey_point'].inc ,  survey_point.inc , ratio_factor ,)) + survey_points[-1]['coordinates'].vs)

    with open('survey_file.csv', 'a') as survey_file:
        writer = csv.writer(survey_file)
        writer.writerow([survey_point.md , survey_point.inc , survey_point.az , coordinates.tvd , coordinates.ns , coordinates.ew , coordinates.vs , ])

    survey_points.append({
        'survey_point': survey_point,
        'coordinates': coordinates,
    })

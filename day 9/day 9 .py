#student_scores = {
    #'Harry': 88,
    #'Ron': 78,
    #'Hermione': 95,
    #'Draco': 75,
    #'Neville': 60
#}

#student_grades = {}

#for student in student_scores:
    #score = student_scores[student]
    #if score >= 91:
        #student_grades[student] = 'outstanding'
    #elif score >= 81 :
        #student_grades[student] = 'Exceeds Expectations'
    #elif score >= 71:
        #student_grades[student] = 'acceptable'
    #else:
        #student_grades[student] = 'fail'        

#print(student_grades)    


capital = {
    "France": "Paris",
    "Germany": "Berlin",
        
    }

# nested list in dictionary

#travel_log = {
    #"France": ["paris" , "lille" , "dijon"],
    #"Germany":["stuttgart" , "berlin"],
    
#}

# print lille
# print(travel_log["france"][1])

#nested_list = ["A", "B", ["c", "D"]]
#print(nested_list[2][1])


travel_log = {    
    "France": {
    "cities_visited": ["paris" , "lille" , "dijon"],
    "total_visits": 12 
    },
    "Germany":{
    "cities_visited": ["stuttgart" , "berlin", "hamburg"],
    "total_visits": 5
    },
}

print(travel_log["Germany"]["cities_visited"][2])
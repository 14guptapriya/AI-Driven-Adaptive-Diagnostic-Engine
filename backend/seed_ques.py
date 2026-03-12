from database import questions_collection
questions = [

# EASY QUESTIONS

{
"question":"What is 5 + 7?",
"options":["10","11","12","13"],
"correct_answer":"12",
"difficulty":0.1,
"topic":"Arithmetic",
"tags":["addition"]
},

{
"question":"What is 9 × 6?",
"options":["42","54","63","56"],
"correct_answer":"54",
"difficulty":0.2,
"topic":"Arithmetic",
"tags":["multiplication"]
},

{
"question":"What is sqrt(49)?",
"options":["5","6","7","8"],
"correct_answer":"7",
"difficulty":0.25,
"topic":"Algebra",
"tags":["square root"]
},

{
"question":"If x + 4 = 10, what is x?",
"options":["4","5","6","7"],
"correct_answer":"6",
"difficulty":0.3,
"topic":"Algebra",
"tags":["equation"]
},

{
"question":"Synonym of 'Big'?",
"options":["Small","Large","Tiny","Weak"],
"correct_answer":"Large",
"difficulty":0.2,
"topic":"Vocabulary",
"tags":["synonym"]
},

# MEDIUM QUESTIONS

{
"question":"What is 15% of 200?",
"options":["20","25","30","35"],
"correct_answer":"30",
"difficulty":0.4,
"topic":"Arithmetic",
"tags":["percentage"]
},

{
"question":"What is 12²?",
"options":["124","144","164","154"],
"correct_answer":"144",
"difficulty":0.45,
"topic":"Algebra",
"tags":["square"]
},

{
"question":"If 2x = 14, what is x?",
"options":["5","6","7","8"],
"correct_answer":"7",
"difficulty":0.5,
"topic":"Algebra",
"tags":["linear equation"]
},

{
"question":"Synonym of 'Rapid'?",
"options":["Slow","Fast","Heavy","Weak"],
"correct_answer":"Fast",
"difficulty":0.5,
"topic":"Vocabulary",
"tags":["synonym"]
},

{
"question":"What is the average of 10, 20, and 30?",
"options":["15","20","25","30"],
"correct_answer":"20",
"difficulty":0.55,
"topic":"Arithmetic",
"tags":["average"]
},

{
"question":"If x - 5 = 9, what is x?",
"options":["12","13","14","15"],
"correct_answer":"14",
"difficulty":0.6,
"topic":"Algebra",
"tags":["equation"]
},

{
"question":"Antonym of 'Strong'?",
"options":["Powerful","Weak","Heavy","Hard"],
"correct_answer":"Weak",
"difficulty":0.45,
"topic":"Vocabulary",
"tags":["antonym"]
},

# HARD QUESTIONS

{
"question":"If 3x - 7 = 11, what is x?",
"options":["4","5","6","7"],
"correct_answer":"6",
"difficulty":0.7,
"topic":"Algebra",
"tags":["equation"]
},

{
"question":"What is the derivative of x²?",
"options":["x","2x","x²","2"],
"correct_answer":"2x",
"difficulty":0.8,
"topic":"Calculus",
"tags":["derivative"]
},

{
"question":"If a train travels 60 km in 1.5 hours, what is its speed?",
"options":["30 km/h","40 km/h","50 km/h","60 km/h"],
"correct_answer":"40 km/h",
"difficulty":0.65,
"topic":"Arithmetic",
"tags":["speed"]
},

{
"question":"What is 7³?",
"options":["343","243","441","512"],
"correct_answer":"343",
"difficulty":0.7,
"topic":"Algebra",
"tags":["cube"]
},

{
"question":"Antonym of 'Scarce'?",
"options":["Rare","Abundant","Tiny","Weak"],
"correct_answer":"Abundant",
"difficulty":0.75,
"topic":"Vocabulary",
"tags":["antonym"]
},

{
"question":"If 5x + 10 = 35, what is x?",
"options":["3","4","5","6"],
"correct_answer":"5",
"difficulty":0.65,
"topic":"Algebra",
"tags":["equation"]
},

{
"question":"What is log₁₀(100)?",
"options":["1","2","10","100"],
"correct_answer":"2",
"difficulty":0.85,
"topic":"Mathematics",
"tags":["logarithm"]
},

{
"question":"What is the next prime number after 23?",
"options":["25","27","29","31"],
"correct_answer":"29",
"difficulty":0.6,
"topic":"Number Theory",
"tags":["prime"]
}

]
questions_collection.insert_many(questions)

print("Questions inserted")
questions= [["A group of stars is called ?","Solar system","Constellation", "Universe","Galaxy", "b"],
            ["Which is the national river of INDIA ?","Yamuna","Brahamputra","Ganga","Saraswati","c"],
            ["Which animal is known as the king of jungle ?","Tigar","Elephant","Cheetah","Lion","d"],
            ["How many continents are there in the world ?","5","7","8","6","b"],
            ["Which gas do humans inhale ?","Oxygen","Carbon Dioxide","Nitrogen","Helium","a"],
            ["When is republic day celebrated ?","15th August","26th August","15th January","26th January","d"],
            ["Who is the father of nation ?","Pt. Jawahar lal Nehru","Mahatma Gandhi","Subhash Chandra Bose","Dr. APJ Abdul Kalam","b"],
            ["Which organ pumps blood ?","Heart","lungs","Kidney","Liver","a"],
            ["What is the closest planet to the Sun ?","Mercury","Venus","Earth","Jupiter","a"],
            ["What is the capital of Japan ?","New Delhi","Tokyo","Beijing","New York","b"],
            ["Who was the player of the match in 2011 World Cup final ?","Gautam Gambhir","Yuvraj Singh","Suresh Raina","MS Dhoni","d"],
            ["Which of the following is not the neighbour-country of India ?","Pakistan","China","Russia","Afghanistan","c"],
            ["In which continent India belongs to ?","Australia","Africa","Europe","Asia","d"],
            ["How many times Shri Narendra Modi won the elections of Lok Sabha ?","1","2","3","4","c"],
            ["Who is the largest mammal in the world ?","Whale","Shark","Blue Whale","Cold fish","c"],
            ["Who was the first person to set foot on the moon ?","Rakesh Sharma","Neil Armstrong","George Washington","Rahul Shah","b"]
            ]
total_prise_won=0
amount=[1000,2000,3000,5000,10000,20000,40000,80000,160000,320000,640000,1250000,2500000,5000000,10000000,70000000]
for x in range(len(questions)):
    print(questions[x][0],"\n a)", questions[x][1],"\t b)", questions[x][2],"\n c)", questions[x][3],"\t d)", questions[x][4],)
    reply= input("Enter your answer :- ")
    if(reply==questions[x][-1]):
        print("correct ansawer")
        print(f"You won {amount[x]} ")
        total_prise_won=amount[x]
    else:
        print("wrong answer")
        break
print(f"Your Winning Amount is {total_prise_won}")

  

             
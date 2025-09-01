questions= [["A group of stars is called ?","Solar system","Constellation", "Universe","Galaxy", "b"],
            ["Which is the national river of INDIA","Yamuna","Brahamputra","Ganga","Saraswati","c"],
            ["Which animal is known as the king of jungle?","Tigar","Elephant","Cheetah","Lion","d"],
            ["How many continents are there in the world?","5","7","8","6","b"],
            ["Which gas do humans inhale?","Oxygen","Carbon Dioxide","Nitrogen","Helium","a"],
            ["When is republic day celebrated?","15th August","26th August","15th January","26th January","d"],
            ["Who is the father of nation?","Pt. Jawahar lal Nehru","Mahatma Gandhi","Subhash Chandra Bose","Dr. APJ Abdul Kalam","b"],
            ["Which organ pumps blood?","Heart","lungs","Kidney","Liver","a"]
            ]
total_prise_won=0
amount=[1000,2000,4000,8000,16000,30000,60000,120000]
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
  

             
// DOM (Document Object Model) არის ობიექტის მოდელი,
//რომელიც აღგვიწერს HTML დოკუმენტის სტრუქტურას და საშუალებას გვაძლევს შევცვალოთ და 
//მანიპულირება გავუწიოთ მას JavaScript-ის მეშვეობით.

        // წვდომა პარაგრაფზე DOM-ის დახმარებით
        const paragraph = document.getElementById('myParagraph');

        // ტექსტის შიგთავსი
        paragraph.textContent = "ამიტომ, ტექსტი შეცვლილია!";

        // ვიზუალური მხარე
        paragraph.style.color = "red"; // ტექსტის ფერის შეცვლა
        paragraph.style.fontSize = "25px"; // ტექსტის ზომის შეცვლა
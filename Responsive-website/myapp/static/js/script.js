
    $(document).ready(function(){
      // Auto play carousel
      console.log("ghj");
      $('.carousel').carousel({
        interval: 1000 // Change interval (time in milliseconds)
        
      });
      document.getElementById("searchForm").addEventListener("submit", function(event) {
        event.preventDefault(); // Prevent form submission
        var searchTerm = document.getElementById("searchInput").value.trim();
        // console.log("jj");
        if (searchTerm.toLowerCase() == "instagram") {
          window.location.href = "https://www.instagram.com";
        } 
        else if(searchTerm.toLowerCase() == "youtube") {
          window.location.href = "https://www.youtube.com";
        } 
        else if(searchTerm.toLowerCase() == "facebook") {
          window.location.href = "https://www.facebook.com/";
        } 
        else if(searchTerm.toLowerCase() == "wikipedia") {
          window.location.href = "https://en.wikipedia.org/wiki/Website";
        } 
        else if(searchTerm.toLowerCase() == "twitter") {
          window.location.href = "https://twitter.com/?lang=en";
        } 
        else if(searchTerm.toLowerCase() == "amazon") {
          window.location.href = "https://www.amazon.in/";
        } 
        else if(searchTerm.toLowerCase() == "whatsapp") {
          window.location.href = "https://www.whatsapp.com/";
        } 
        else if(searchTerm.toLowerCase() == "google") {
          window.location.href = "https://www.google.com/";
        } 
        else if(searchTerm.toLowerCase() == "linkedin") {
          window.location.href = "https://in.linkedin.com/";
        } 
        else if(searchTerm.toLowerCase() == "bing") {
          window.location.href = "https://www.bing.com/";
        } 
        else if(searchTerm.toLowerCase() == "yahoo") {
          window.location.href = "https://in.search.yahoo.com/";
        } 
        else if(searchTerm.toLowerCase() == "netflix") {
          window.location.href = "https://www.netflix.com/in/";
        }
        else if(searchTerm.toLowerCase() == "microsoft") {
          window.location.href = "https://www.microsoft.com/en-in";
        }
        else if(searchTerm.toLowerCase() == "aws") {
          window.location.href = "https://aws.amazon.com/";
        }
        else if(searchTerm.toLowerCase() == "mozilla") {
          window.location.href = "https://developer.mozilla.org/en-US/";
        }
        else if (searchTerm.toLowerCase() == ""){
          alert("search only popular website dont left empty")
        }
        else {
          // Handle other search terms or provide feedback to the user
          alert("Sorry, this search feature is only for popular sites.");
        }
      });
    });



      
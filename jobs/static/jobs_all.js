$(document).ready(function(){

    $.ajax({
    type: "GET",
    url:"/newCompanies",
    data: {csrfmiddlewaretoken: '{{ csrf_token }}'},
    contentType: "text",
    dataType : "text",
    success: function(newCompanies){            

                     
        $(".container").append(newCompanies);

        }
    });


 });



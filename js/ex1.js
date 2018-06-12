$("#jerusalemPost").click( function() {
console.log(document.cookie)
    $.ajax({
            type: "GET",
            dataType: 'json',
            url: "http://localhost:7000/api/getFeedsJP",

            success: function (response) {
                $("#text").text("you last refreshed your headlines feed at " + document.cookie.slice(14,-11))
                $("#app").empty()
                for (var i = 0; i < response.length; i++) {
                       var newDiv=$("<div>")
                       var headlines=$("<a>")
                       newDiv.addClass("nameBox")
                       headlines.text(response[i]["titles"])
                       headlines.attr("href",response[i]["link"])
                       $("#app").append(newDiv)
                       newDiv.append(headlines)
                    }
                    console.log(response)
                },
            error: function (msg) {
                console.log(msg);
            },
            complete: function (response, status) {
                console.log("complete");
            }
        });
    });

$("#wallStreet").click( function() {
    $.ajax({
            type: "GET",
            dataType: 'json',
            url: "http://localhost:7000/api/getFeedsDM",

            success: function (response) {
                $("#text").text("you last refreshed your headlines feed at " + document.cookie.slice(14,-11))
                $("#app").empty()
                for (var i = 0; i < response.length; i++) {
                       var newDiv=$("<div>")
                       var headlines=$("<a>")
                       newDiv.addClass("nameBox")
                       headlines.text(response[i]["titles"])
                       headlines.attr("href",response[i]["link"])
                       $("#app").append(newDiv)
                       newDiv.append(headlines)
                    }
                    console.log(response)
                },
            error: function (msg) {
                console.log(msg);
            },
            complete: function (response, status) {
                console.log("complete");
            }
        });
    });

$("#refresh").click(function(){
    location.reload()
})
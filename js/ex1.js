$( document ).ready(function() {
    $("#jerusalemPost").click( function() {
        $.ajax({
            type: "GET",
            dataType: 'json',
            url: "http://localhost:7001/api/getFeedsJP",

            success: function (response) {
            console.log(response)
                var feed = response[0]
                var last_seen = response[1]
                 $("#text").text(last_seen)
                $("#app").empty()
                for (var i = 0; i < feed.length; i++) {
                       var newDiv=$("<li>")
                       var headlines=$("<a>")
                       newDiv.addClass("nameBox")
                       headlines.text(feed[i]["titles"])
                       headlines.attr("href",feed[i]["link"])
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
            url: "http://localhost:7001/api/getFeedsDM",

            success: function (response) {
            console.log(response)
                var feed = response[0]
                var last_seen = response[1]
                $("#text").text(last_seen)
                $("#app").empty()
                for (var i = 0; i < feed.length; i++) {
                       var newDiv=$("<li>")
                       var headlines=$("<a>")
                       newDiv.addClass("nameBox")
                       headlines.text(feed[i]["titles"])
                       headlines.attr("href",feed[i]["link"])
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
    });
});


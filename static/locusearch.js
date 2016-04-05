    function getSearchValue() {
    var city = document.getElementById("mySearch").value;
    var str1 = "https://api.locu.com/v1_0/venue/search/?locality=";
    var str2 = "&category=restaurant&api_key=";
    var apiKey = "dad8814e20be289b1b53b60ca73c7e3735574370";
    var URL = str1.concat(city).concat(str2).concat(apiKey);
    //document.getElementById("demo").innerHTML = URL;


    $( document ).ready(function() {
    $.ajax({
      url: URL,
      crossDomain: true,
        dataType: 'jsonp',
    }).done(function(res) {
      console.log(res.objects)
      for(i=0;i<res.objects.length;i++) {
        //x = res.objects[i].name
        //console.log(x)
        //document.getElementById("demo").innerHTML = res.objects[i].name + "<br>" 
        $("p").append("<li id='name'>" + res.objects[i].name + "</li>")
        $("p").append("<li id='address'>" + res.objects[i].street_address + ", " + res.objects[i].locality + ", " + res.objects[i].region +"</li>")
        $("p").append("<li id='phone'>" + res.objects[i].phone + "</li><br>")


      }
    });

})



}
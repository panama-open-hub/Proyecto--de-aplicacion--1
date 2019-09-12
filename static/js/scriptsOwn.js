function foo() //onload="foo()"
{
alert("Page is loaded");
}

//onclick="updateDashboardFnc(); return false;"
function updateDashboardFnc() {
    dt = getDate();
    document.getElementById("updateLabel").innerHTML =dt;
    let value = 'Pablo'
    $.ajax({
        url: "//localhost:5000/postdata",
        type: "POST",
        data: {
            session: value,
            action: 'change'
        },
        dataType: 'json',
        success: function(data){
            console.log("success");
            console.log(data);
        },
        failure: function(data){
            console.log("failure");
            console.log(data);
        },
    });
}

function updateDashboardFnc_Original() {
    dt = getDate();
    document.getElementById("updateLabel").innerHTML =dt;
    let value = 'Pablo'
    $.ajax({
        url: "//localhost:5000/postdata",
        type: "POST",
        data: {
            session: value,
            action: 'change'
        },
        dataType: 'json',
        success: function(data){
            console.log("success");
            console.log(data);
        },
        failure: function(data){
            console.log("failure");
            console.log(data);
        },
    });
}

var months = [
    'January', 'February', 'March', 'April', 'May',
    'June', 'July', 'August', 'September',
    'October', 'November', 'December'
    ];

function getDate() {
    var today = new Date();
    var date =monthNumToName((today.getMonth()+1))+' '+today.getDate()+', '+today.getFullYear();
    var time = formatAMPM(today)
    var dateTime = date+' '+time;
    return dateTime;
}

function monthNumToName(monthnum) {
    return months[monthnum - 1] || '';
}
function monthNameToNum(monthname) {
    var month = months.indexOf(monthname);
    return month ? month + 1 : 0;
}

function formatAMPM(date) {
    var hours = date.getHours();
    var minutes = date.getMinutes();
    var ampm = hours >= 12 ? 'pm' : 'am';
    hours = hours % 12;
    hours = hours ? hours : 12; // the hour '0' should be '12'
    minutes = minutes < 10 ? '0'+minutes : minutes;
    var strTime = hours + ':' + minutes + ' ' + ampm;
    return strTime;
  }
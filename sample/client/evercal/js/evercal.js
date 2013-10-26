function fillCalendar(div_id, cal) {
  // mooECal has a weird API.
  cal.calContainer = div_id;
  new Calendar(cal);
}

jQuery.noConflict();
jQuery.ajaxSetup({
  error: function(jqXHR, textStatus, errorThrown) {
    console.log("error: " + textStatus);
  }
});
window.addEvent('domready', function() {
  jQuery.getJSON('http://localhost:8000/cgi-bin/EDAMTest.py', function(data) {
    fillCalendar('calendar', {
      cEvents: data
    });
  });
});

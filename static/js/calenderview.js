$(document).ready(function () {
    var calendar = $('#calendar').fullCalendar({
        header: {
            left: 'prev,next today',
            center: 'title',
            right: 'month,agendaWeek,agendaDay'
        },
        events: '/all_cases',
        selectable: true,
        selectHelper: true,
        editable: true,
        eventLimit: true,
        select: function (start, end, allDay) {

            // Show the modal
            $('#eventModal').modal('show');

            // Unselect the date on the calendar
            calendar.fullCalendar('unselect');
        },


    });


       

});
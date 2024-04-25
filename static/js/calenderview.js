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


        eventClick: function (calEvent, jsEvent, view) {
            // Show the modal
            $('#eventModal').modal('show');
    
            // Populate the form fields with event data
            $('#id_alien_number').val(calEvent.alien_number);
            $('#id_first_name').val(calEvent.first_name);
            $('#id_middle_name').val(calEvent.middle_name);
            $('#id_last_name').val(calEvent.last_name);
            $('#id_phone_number').val(calEvent.phone_number);
            $('#id_email').val(calEvent.email);
            $('#id_Address').val(calEvent.Address);
            $('#id_city').val(calEvent.city);
            $('#id_zipcode').val(calEvent.zipcode);
            $('#id_country').val(calEvent.country);
            $('#id_type_of_case').val(calEvent.type_of_case);
            $('#id_i_589_filed').val(calEvent.i_589_filed);
            $('#id_erop').val(calEvent.erop);
            $('#id_e_28_filed').val(calEvent.e_28_filed);
            $('#id_biometrics_filed').val(calEvent.biometrics_filed);
            $('#id_foia_submitted').val(calEvent.foia_submitted);
            $('#id_foia_uploaded').val(calEvent.foia_uploaded);
            $('#id_work_permit_applied').val(calEvent.work_permit_applied);
            $('#id_hearing_location').val(calEvent.hearing_location);
            $('#id_total_billing_amount').val(calEvent.total_billing_amount);
            $('#id_amount_paid').val(calEvent.amount_paid);
            $('#id_date').val(calEvent.date);
    
            // Update form action for case update
            $('#caseForm').attr('action', '/update_case/' + calEvent.id);
        }

    



    });

    // Form submission
    $('#caseForm').submit(function (event) {
        event.preventDefault();
        var formData = $(this).serialize();
        var url = $(this).attr('action');

        $.ajax({
            type: 'POST',
            url: url,
            data: formData,
            success: function (response) {
                $('#eventModal').modal('hide');
                calendar.fullCalendar('refetchEvents');
            },
            error: function (xhr, errmsg, err) {
                console.log(xhr.status + ': ' + xhr.responseText);
            }
        });
    });
    
    
    




});
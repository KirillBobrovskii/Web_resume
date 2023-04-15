$(function() {
    var index = 0;

    $('#left').click(function() {
        if (index > 0) {
            index -= 1;
        } else {
            index = count_projects - 1;
        }
        ajax(index);
    });

    $('#right').click(function() {
        if (index < count_projects - 1) {
            index += 1;
        } else {
            index = 0;
        }
        ajax(index);
    });

    function ajax(index) {
        $.ajax({
            url: projects_slider_url,
            data: {
                index: index
            },
            success: function (project) {
                $('#projects h3').text(project.project),
                $('#projects img').attr('src', project.image),
                $('#projects a').attr('href', project.slug)
            },
            error: function (project) {
                console.log(project.responseJSON.errors);
            }
        });
    }
});
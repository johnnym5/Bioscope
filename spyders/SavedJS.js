	$.ajax({
							url: '/browseByGenre',
							data : $('form').serialize(),
							type: 'POST',
							success: function(response) {
								var movies = $.parseJSON(response);
								
								$.each(movies, function (index, table) {
									var thumbs = $('<div class="thumbnail">');
									var image = $('<img src = "' + table.Poster + '" width = "182" height = "268">');
									var ref = $('<a href = "#" class = "btn btn-primary col-xs-12" role="button">Info</a>');
									thumbs.append(image);
									thumbs.append(ref);
									thumbs.append('</div>');
									$("#movieList").append(thumbs);
								});
							},
							error: function(error) {
								console.log(error);
							}
						});
$(document).ready(function () {

	var $id_local = $("#id_local");

	$id_local.on('change', (function() {

		if ($("#id_local option:selected").text() == "Numec")
			$id_local.parents('.row').next().hide();

		else
			$id_local.parents('.row').next().show();
	}));
});
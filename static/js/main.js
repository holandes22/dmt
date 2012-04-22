var layoutSettings_Outer = {
	name: "outerLayout",
	defaults: {
	},
	north: {
		spacing_open:			0,
		togglerLength_open:		0,			// HIDE the toggler button
		resizable: 				false,
		maxSize:				25,
		size:					25,
	},
	west: {
		minSize:				250,
		size:					250,
	},
}

$(document).ready(function () {
	
    layout = $('#layout_container').layout( layoutSettings_Outer );
    $.layout.defaults.panes.liveResizing = true;
    
    $( "#ui-layout-west-tabs" ).tabs();
});
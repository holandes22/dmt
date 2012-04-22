var layoutSettings_Outer = {
	name: "outerLayout",
	defaults: {
	},
	north: {
		spacing_open:			0,
		togglerLength_open:		0,			// HIDE the toggler button
		resizable: 				false,
		size:					45,
	},
	west: {
		minSize:				250,
		size:					250,
	},
}

$(document).ready(function () {
	
	/*--------------Layout--------------------------------------------*/
    layout = $( '#layout_container' ).layout( layoutSettings_Outer );
    $.layout.defaults.panes.liveResizing = true;
    
    /*--------------Tabs----------------------------------------------*/
    $( "#ui-layout-west-tabs" ).tabs({
    	select: function(event, ui) {
    		 	$( "#accordion-disks, #accordion-lvm" ).toggle();			 
    		},
    });
    
    //This allows for the border of the tab content to extend to the bottom
    $("#ui-layout-west-tabs").css("min-height", "99%");
    
    /*--------------Accordion------------------------------------------*/
    $( "#accordion-disks" ).accordion({
		fillSpace: true
	});
	$( "#accordion-lvm" ).accordion().hide();
	
    
    
    
    
});
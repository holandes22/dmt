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
		spacing_open:			3,
	},
	east: {
		minSize:				300,
		size:					300,
		spacing_open:			3,
	},
}

$(document).ready(function () {
	
	$( "#sysinfo").load("sysinfo/")
	
	/*--------------Layout--------------------------------------------*/
    layout = $( '#layout_container' ).layout( layoutSettings_Outer );
    $.layout.defaults.panes.liveResizing = true;
    
    /*--------------Tabs----------------------------------------------*/
    $( "#ui-layout-west-tabs" ).tabs({
    	select: function(event, ui) {
	    		var currentTab = $(ui.tab).attr('href');
	    		var pos = currentTab.indexOf("-");
	    		// form selector of selected tab: #accordion-disk, for example
	    		var selector = "#accordion" + currentTab.slice(pos);
	    		$( "#accordion-disks, #accordion-lvm, #accordion-fs" ).hide();
	    		$(selector).show();		 
    		},
    });
    
    //This allows for the border of the tab content to extend to the bottom
    $("#ui-layout-west-tabs").css("min-height", "99%");
    
    /*--------------Accordion------------------------------------------*/
    $( "#accordion-disks" ).accordion({
		fillSpace: true
	});
	$( "#accordion-lvm,#accordion-fs" ).accordion().hide();
	$( "#accordion-right-pane").accordion({
		icons: {
			headerSelected: "ui-icon-info",
            fillSpace: true
		}
	});
	
    
    
    
    
});

CURRENT_TREE_NODE = null;

function reactivateCurrentTreeNode() {
	if(CURRENT_TREE_NODE){
		CURRENT_TREE_NODE.deactivate();
		CURRENT_TREE_NODE.activate();
	}	
}


function errorHandler(node, XMLHttpRequest, textStatus, errorThrown){
	$('#right_pane_content').load(textStatus);
}

function onActivateHandler(node){
	CURRENT_TREE_NODE = node;
	$.ajax({
		url: node.data.url,
		success: function(data, textStatus, jqXHR){
			$('#accordion-disks-details').html(data);	
		},
		error: function(jqXHR, textStatus, errorThrown){
			$('#middle-pane').html(jqXHR.responseText);
		},
	});
}

function onLazyReadHandler(node){
	node.appendAjax({
		url : node.data.lazyLoadingUrl,
		data : {
			"key" : node.data.key,  // Optional url arguments
		},
		error: errorHandler,
	});
}

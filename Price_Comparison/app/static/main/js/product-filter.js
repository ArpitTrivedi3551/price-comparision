$(document).ready(function(){
    $(".ajaxLoader").hide();
    $(".filter-checkbox,#Pricefilterbtn").on('click', function() {
        var _filterObj={};
		var _minPrice=$('#minPricenum').val();
		var _maxPrice=$('#maxPricenum').val();
		_filterObj.minPrice=_minPrice;
		_filterObj.maxPrice=_maxPrice;
		// var _minPrice=$('#maxPrice').attr('min');
		// var _maxPrice=$('#maxPrice').val();
		// _filterObj.minPrice=_minPrice;
		// _filterObj.maxPrice=_maxPrice;
		$(".filter-checkbox").each(function(index,ele){
			var _filterVal=$(this).val();
			var _filterKey=$(this).data('filter');
			_filterObj[_filterKey]=Array.from(document.querySelectorAll('input[data-filter='+_filterKey+']:checked')).map(function(el){
			 	return el.value;
			});
		});

        //Run Ajax

        $.ajax({
            url:'/filter-data/',
			data:_filterObj,
			dataType:'json',
			beforeSend:function(){
				$(".ajaxLoader").show();
			},
			success:function(res){
				console.log(res);
				$("#filted-product").html(res.data);
				$(".ajaxLoader").hide();
			}
        })
    });

	$(".btn.btn-info.btn-sm").on('blur',function(){
		var _min=$(this).attr('min');
		var _max=$(this).attr('max');
		var _minvalue=$("#minPricenum").val();
		var _maxvalue=$("#maxPricenum").val();
		console.log(_minvalue,_maxvalue,_min,_max);
		if(_minvalue < parseInt(_min) || _maxvalue > parseInt(_max)){
			alert('Values should be '+_min+'-'+_max);
			$("#minPricenum").val(_min);
			$("#maxPricenum").val(_max);
			$(this).focus();
			$("#minPricesdr").val(_min);
			$("#maxPricesdr").val(_max);
			return false;
		}
	});
});
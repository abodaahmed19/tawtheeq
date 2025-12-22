$(function(){
	$('#rowSelection').DataTable({
		'iDisplayLength': 10,
		"language": {
			"decimal":        "",
			"emptyTable":     "لا توجد بيانات متاحة في الجدول",
			"info":           "عرض الصفحة _PAGE_ من _PAGES_",
			"infoEmpty":      "عرض 0 إلى 0 من 0 سجل",
			"infoFiltered":   "(منتقاة من مجموع _MAX_ سجلات)",
			"infoPostFix":    "",
			"thousands":      ",",
			"lengthMenu":     "عرض _MENU_ سجلات في كل صفحة",
			"loadingRecords": "جاري التحميل...",
			"processing":     "جاري المعالجة...",
			"search":         "البحث:",
			"zeroRecords":    "لم يتم العثور على سجلات مطابقة",
			"paginate": {
				"first":      "الأول",
				"last":       "الأخير",
				"next":       "التالي",
				"previous":   "السابق"
			},
			"aria": {
				"sortAscending":  ": تفعيل لترتيب العمود تصاعدياً",
				"sortDescending": ": تفعيل لترتيب العمود تنازلياً"
			},
		},
		"columnDefs": [
			{ className: "text-center align-middle", targets: "_all" }
		]
	});
	var table = $('#rowSelection').DataTable();

	$('#rowSelection tbody').on( 'click', 'tr', function () {
		$(this).toggleClass('selected');
	});

	$('#button').on('click', function () {
		alert( table.rows('.selected').data().length +' row(s) selected' );
	});
});

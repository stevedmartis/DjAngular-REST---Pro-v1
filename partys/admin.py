from django.contrib import admin

from .models import Party, Status, Category, Tipo



class PartyModelAdmin(admin.ModelAdmin):
	list_display = ["id", "name", "description", "slug", "createdAt", "updatedAt", "status", "user", "place" ,"address", "location", "eventdate", "category", ]
	list_display_links = ["user", "status", "category",]
	list_editable     = [ "name", "description", "location", "place", "address", ]
	list_filter	       = [ "name" , "status", ]
	filter_horizontal = [ "tipo", ]

	search_fields = ["name", "user"]
	class Meta:
		model = Party 


admin.site.register(Party, PartyModelAdmin)



class StatusModelAdmin(admin.ModelAdmin):
	list_display = ["id", "name",  ]
	list_display_links = ["id", ]
	list_editable     = [ "name",  ]

	search_fields = ["name", ]
	class Meta:
		model = Status 


admin.site.register(Status, StatusModelAdmin)



class CategoryModelAdmin(admin.ModelAdmin):
	list_display = ["id", "name",  ]
	list_display_links = ["id", ]
	list_editable     = [ "name",  ]

	search_fields = ["name", ]
	class Meta:
		model = Category 


admin.site.register(Category, CategoryModelAdmin)

class TipoModelAdmin(admin.ModelAdmin):
	list_display = ["id", "name",  ]
	list_display_links = ["id", ]
	list_editable     = [ "name",  ]

	search_fields = ["name", ]
	class Meta:
		model = Tipo 


admin.site.register(Tipo, TipoModelAdmin)
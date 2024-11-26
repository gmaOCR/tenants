from django.shortcuts import render

def tenant_info_view(request):
    return render(request, 'tenant_info.html', {
        'tenant': request.tenant,
        'schema_name': connection.schema_name
    })
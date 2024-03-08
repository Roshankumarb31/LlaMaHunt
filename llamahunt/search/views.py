from django.shortcuts import render
from django.http import HttpResponse

from .models import FilesUpload, JobApplication
# import shutil


# Create your views here.


def JobApplication(data):
    [job_type, work_preference, resume, additional_info ] = data
    
    job_application_instance = []
    
    instance = {'job_name' : 'engineer',
            'job_type' : 'job',
            'work_preference' : 'onsite',
            'company_name' : 'nvdia',
            'comp_desc' : 'best company ever in the world',
            'apply_link' : 'www.google.com'}
    
    job_application_instance.append(instance)
    
    return job_application_instance


def credentials(request):
    return render(request, 'credentials.html')

def results(request):
    job_type = request.POST.get('job_type')
    work_preference = request.POST.get('work_preference')
    
    
    resume = request.FILES['resume']
    document = FilesUpload.objects.create(file = resume)
    document.save()
    
    # form = UploadFileForm(request.POST, request.FILES)
    # if form.is_valid():
    #     uploaded_file = request.FILES.get['file']
    #     # Specify the directory where you want to save the file
    #     save_path = 'G:\\one-api\\llamahunt\\static'  # Update this with your desired directory path
    #     # Ensure that the directory exists, create if it doesn't
    #     if not os.path.exists(save_path):
    #         os.makedirs(save_path)
    #     # Save the file to the specified location
    #     file_path = os.path.join(save_path, uploaded_file.name)
    #     with open(file_path, 'wb') as f:
    #         for chunk in uploaded_file.chunks():
    #             f.write(chunk)
        
        
        
        
        
        # uploaded_file = request.FILES['file']
        # # Now you can handle the uploaded file
        # # For example, you can save it to disk
        # with open('uploaded_file.pdf', 'wb') as f:
        #     for chunk in uploaded_file.chunks():
        #         f.write(chunk)
                    
                    
    # resume = request.FILES.get('resume')
    # if resume==None:
    #     print('true')
    
    # # resume_name = resume.name()
    # # pdf_file_path = 'path/to/your/pdf/file.pdf'
    # extracted_text = extract_text_from_pdf(resume)
    # print(extracted_text)
    
    
    # source_destination = 'G:\one-api\llamahunt\static'
    # # source_file = os.path.join(source_directory, resume_name)
    
    # destination_directory = 'G:\one-api\llamahunt\static'
    
    # destination_file = os.path.join(destination_directory, resume_name)

    # shutil.copyfile(source_file, destination_file)
    
    
    

    additional_info = request.POST.get('additional_info')
    data = {'job_type':job_type,
        'work_preference':work_preference,
        'resume':resume.name,
        'additional_info':additional_info
    }
    print(data)
    # print(**data)
    
    # job_application_instance = JobApplication(**data)
    
    # print(job_application_instance)
    
    job_application_instance = [{'job_title': 'Software engineer, new grad', 'company_name': 'Watershed', 'location': 'San Francisco, CA', 'salary_info': 'Salary Info not available', 'link': 'https://www.linkedin.com/company/watershedclimate?trk=public_jobs_jserp-result_job-search-card-subtitle'}, 
                                {'job_title': 'Entry Level Software Engineer (Remote)', 'company_name': 'Engtal', 'location': 'United States', 'salary_info': 'Salary Info not available', 'link': 'https://www.linkedin.com/company/engtal?trk=public_jobs_jserp-result_job-search-card-subtitle'}, 
                                {'job_title': 'Software Developer(Junior Level)', 'company_name': 'SynergisticIT', 'location': 'United States', 'salary_info': 'Salary Info not available', 'link': 'https://www.linkedin.com/company/synergisticit?trk=public_jobs_jserp-result_job-search-card-subtitle'}]            
    
    
    return render(request, 'results.html', {'data' : job_application_instance})

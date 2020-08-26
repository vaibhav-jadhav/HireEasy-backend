from django.db import models
class Jobs(models.Model):
    title = models.CharField(max_length=60)
    company = models.CharField(max_length=60)
    post= models.CharField(max_length=60)
    exp= models.CharField(max_length=60)
    desc= models.CharField(max_length=500)
    resp= models.CharField(max_length=200)
    skills= models.CharField(max_length=60)
    def get_model_fields(model):
        return model._meta.fields 
class Applications(models.Model):
    jobid = models.CharField(max_length=10)
    full_name = models.CharField(max_length=60)
    email = models.CharField(max_length=60)
    address = models.CharField(max_length=60)
    phone = models.CharField(max_length=60)
    resume = models.CharField(max_length=60)
    status= models.CharField(max_length=60)
    applyid=models.CharField(max_length=50)
    feedback=models.CharField(max_length=300)
    def get_model_fields(model):
        return model._meta.fields 
class Interview(models.Model):
    applyid = models.CharField(max_length=30)
    title = models.CharField(max_length=250)
    link = models.CharField(max_length=100)
    time = models.CharField(max_length=30)
    note = models.CharField(max_length=250)
    def get_model_fields(model):
        return model._meta.fields 
    #   this.prev_state['applyid']+
    #   this.title+
    #   this.link+
    #   this.time+
    #   this.note);
    
#   const data =[{
#         "id":this.prev_state["id"],
#         "full_name":this.Name,
#         "email": this.Email,
#         "address":this.Adress,
#         "phone":this.phone,
#         "resume":this.resume,
#         }];
   
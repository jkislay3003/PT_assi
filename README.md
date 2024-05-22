# PT_assi
# Setup Instructions
- Clone the project
  -git clone https://github.com/jkislay3003/PT_assi.git
-Install dependices
  - pip install -r requirements.txt
- Apply migration
- Run the server
  - python manage.py runserver
# EndPoint 

- Users Endpoint:

   - GET /api/users/<user_id>/: Retrieve user details.
   - POST /api/users/: Create a new user.
   - PUT /api/users/<user_id>/: Update user details.
   - DELETE /api/users/<user_id>/: Delete a user.
   -GET /api/users/<user_id>/home_feed/: Generate personalized  home feed for the user.

- Children Endpoint:

   - GET /api/children/<child_id>/: Retrieve child details.
   - POST /api/children/: Add a new child.
   - PUT /api/children/<child_id>/: Update child details.
   - DELETE /api/children/<child_id>/: Delete a child.
- Blogs Endpoint:

    - GET /api/blogs/<blog_id>/: Retrieve blog details.
    - POST /api/blogs/: Create a new blog.
    - PUT /api/blogs/<blog_id>/: Update blog details.
    - DELETE /api/blogs/<blog_id>/: Delete a blog.
- Setting Perefernce 
    curl -X POST http://127.0.0.1:8000/api/users/1/set_preferences/ \
    -H "Content-Type: application/json" \
    -d '{"preferences": {"content_type": ["blog", "vlog"]}}'

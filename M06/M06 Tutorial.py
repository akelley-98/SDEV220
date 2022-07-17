<!DOCTYPE html>
<html>
    <head>
        <title>  {{ title }} </title>
        <style>
        body{
            background-color: #45a254;
        }

        h1{
            color: #eaeaea;
        }
        </style>
    </head>

    <body>
        {% if message %}
            <h1> {{ message }}  </h1>
        {% else %}
            <h1> default message </h1>
        {% endif %}

        <form>
            <button>Click Me</button>
            <input type="checkbox" value="checker"/>
        </form>
    </body>
</html>
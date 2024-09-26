#!/usr/bin/env python

html_code = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Registration Page</title>
</head>
<body bgcolor="lightyellow">
    <br>
    <br>
    <form>
        <label>Firstname:</label>
        <input type="text" name="firstname" size="15"/><br><br>
        <label>Middlename:</label>
        <input type="text" name="middlename" size="15"/><br><br>
        <label>Lastname:</label>
        <input type="text" name="lastname" size="15"/><br><br>

        <label>Course:</label>
        <select>
            <option value="Course">Course</option>
            <option value="BCA">BCA</option>
            <option value="BBA">BBA</option>
            <option value="B.Tech">B.Tech</option>
            <option value="MBA">MBA</option>
            <option value="MCA">MCA</option>
            <option value="M.Tech">M.Tech</option>
        </select><br><br>

        <label>Gender:</label><br>
        <input type="radio" name="gender" value="male"/> Male<br>
        <input type="radio" name="gender" value="female"/> Female<br>
        <input type="radio" name="gender" value="other"/> Other<br><br>

        <label>Phone:</label>
        <input type="text" name="country_code" value="+91" size="2"/>
        <input type="text" name="phone" size="10"/><br><br>

        <label>Address:</label><br>
        <textarea cols="80" rows="5" name="address"></textarea><br><br>

        <label>Email:</label>
        <input type="email" id="email" name="email"/><br><br>

        <label>Password:</label>
        <input type="password" id="pass" name="pass"/><br><br>

        <label>Re-type password:</label>
        <input type="password" id="repass" name="repass"/><br><br>

        <input type="submit" value="Submit"/>
    </form>
</body>
</html>
"""

with open('registration.html', 'w') as f:
    f.write(html_code)

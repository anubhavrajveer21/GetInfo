from flask import Flask

App = Flask(__name__)

@App.route("/")
def Main():
    return '''
  <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Informant</title>
    <style>
        *
{
    margin: 0;
    padding: 0;
    box-sizing: border-box;
    font-family: 'arial', sans-serif;
}

section{
    position: relative;
    width: 100%;
    display: flex;
    justify-content: center;
    align-items: center;
    min-height: 100vh;
    background-color: blue;/* For browsers that do not support gradients */
    background-image: linear-gradient(to right, #009dff, #0004ff00);
}

section header{
    position: absolute;
    top: 0;
    width: 100%;
    display: flex;
    justify-content: flex-end;
    padding: 20px;
}

section header ul{
    display: flex;
    justify-content: center;
    align-items: center;
}

section header ul li{
    list-style: none;
    margin-left: 20px;
}

section header ul li a{
    color: rgb(255, 255, 255);
    text-decoration: none ;
    font-size: 13px;
}

.invisible{
    visibility: hidden;
}

section header ul li button{
    background: #4584ef;
    border: none;
    outline: none;
    padding: 8px 14px;
    color: #fff;
    font-size: 14px;
    font-weight: 700;
    border-radius: 3px;
    cursor: pointer;
}

section .main {
    width: 580px;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
}

section .main .searchBox{
    position: relative;
    width: 100%;
    margin-top: 20px;
}

section .main .searchBox .search{ 
    width: 100%;
    padding: 13px;
    padding-Left: 45px;
    padding-right: 60px;
    border-radius: 30px;
    border: 1px solid #ccc;
    outline: none;
    font-size: 16px;
}

section .main .searchBox .icons{
    position: absolute;
    top: 0;
    width: 100%;
    display: flex;
    padding: 12px 20px;
    justify-content: space-between;
    align-items: center;
    pointer-events: none;
}

section .main .buttons{
    margin-top: 20px;
}

section .main .buttons button{
    margin: 0 5px;
    padding: 12px 20px;
    color: #555;
    font-size: 14px;
    border: none;
    cursor: pointer;
    border-radius: 4px;
    border: 1px solid transparent;
    outline: none;
}

section .main .buttons button:hover{
    border: 1px solid #ccc;
}
    </style>
</head>
<body>
    <section>
        <header>
            <ul>
                <li><a href="#about" class="">About</a></li>
                <li><a href="#blogs" class="">Blog</a></li>
                <li><a href="#team" class="">Our Team</a></li>
                <li><button>Sign in</button></li>
            </ul>
        </header>
        <div class="main">
            <img src="website/Images/logo11.png">
            <div class="searchBox">
                <div class="search-wrapper">
                    <input type="search" class="search" id="search">
                </div>
                <div class="icons">
                    <div><img class="invisible" src="website/Images/search.png"></div>
                    <div><img src="website/Images/search.png"></div>
                </div>
            </div> 
            <div class="buttons">
                <button>Informant Search</button>
                <button>I'm feeling lucky</button>
            </div>
        </div>
    </section>
</body>
</html>
'''

@App.route("/error")
def Result():
  return '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <script src="https://cdn.tailwindcss.com"></script>
    <title>Informant - 404 Error!</title>
</head>
<body>
    <header class="text-gray-200 bg-blue-500 body-font">
        <div class="container mx-auto flex flex-wrap p-5 flex-col md:flex-row items-center">
          <a class="flex title-font transition ease-in-out delay-300 hover:-translate-y-1 hover:scale-110 cursor-pointer duration-300  font-medium items-center text-white mb-4 md:mb-0">
            <span class="ml-3 text-3xl">TechnoBeast</span>
          </a>
          <nav class="md:ml-auto flex flex-wrap items-center text-base justify-center">
            <a class="mr-5 transition ease-in-out delay-300 hover:-translate-y-1 hover:scale-110 cursor-pointer duration-300 hover:text-white">Home</a>
            <a class="mr-5 transition ease-in-out delay-300 hover:-translate-y-1 hover:scale-110 cursor-pointer duration-300 hover:text-white">About</a>
            <a class="mr-5 transition ease-in-out delay-300 hover:-translate-y-1 hover:scale-110 cursor-pointer duration-300 hover:text-white">Our Team</a>
            <a class="mr-5 transition ease-in-out delay-300 hover:-translate-y-1 hover:scale-110 cursor-pointer duration-300 hover:text-white">How It Works?</a>
          </nav>
          <button class="inline-flex transition ease-in-out delay-300 hover:-translate-y-1 hover:scale-110 cursor-pointer duration-300 items-center bg-gray-800 border-0 py-1 px-3 focus:outline-none hover:drop-shadow-lg hover:bg-gray-700 rounded text-base mt-4 md:mt-0">Sign In
            <svg fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" class="w-4 h-4 ml-1" viewBox="0 0 24 24">
              <path d="M5 12h14M12 5l7 7-7 7"></path>
            </svg>
          </button>
        </div>
    </header>
    <section class="text-gray-600 body-font">
        <div class="container mx-auto flex px-5 py-24 items-center justify-center flex-col">
          <div class="text-center lg:w-2/3 w-full">
            <h1 class="title-font sm:text-4xl text-3xl mb-4 font-medium text-gray-900">404</h1>
            <p class="mb-8 leading-relaxed">The link that you are trying to open doesn't exists</p>
            <div class="flex justify-center">
              <button class="inline-flex text-white bg-green-500 border-0 py-2 px-6 focus:outline-none hover:bg-green-300 rounded text-lg">Go To Home Page</button>
            </div>
          </div>
        </div>
    </section>
</body>
</html>
'''

@App.route("/notsafe")
def NotSafe():
  return '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <script src="https://cdn.tailwindcss.com"></script>
    <title>Informant - Not Safe!</title>
</head>
<body>
    <header class="text-gray-200 bg-blue-500 body-font">
        <div class="container mx-auto flex flex-wrap p-5 flex-col md:flex-row items-center">
          <a class="flex title-font transition ease-in-out delay-300 hover:-translate-y-1 hover:scale-110 cursor-pointer duration-300  font-medium items-center text-white mb-4 md:mb-0">
            <span class="ml-3 text-3xl">TechnoBeast</span>
          </a>
          <nav class="md:ml-auto flex flex-wrap items-center text-base justify-center">
            <a class="mr-5 transition ease-in-out delay-300 hover:-translate-y-1 hover:scale-110 cursor-pointer duration-300 hover:text-white">Home</a>
            <a class="mr-5 transition ease-in-out delay-300 hover:-translate-y-1 hover:scale-110 cursor-pointer duration-300 hover:text-white">About</a>
            <a class="mr-5 transition ease-in-out delay-300 hover:-translate-y-1 hover:scale-110 cursor-pointer duration-300 hover:text-white">Our Team</a>
            <a class="mr-5 transition ease-in-out delay-300 hover:-translate-y-1 hover:scale-110 cursor-pointer duration-300 hover:text-white">How It Works?</a>
          </nav>
          <button class="inline-flex transition ease-in-out delay-300 hover:-translate-y-1 hover:scale-110 cursor-pointer duration-300 items-center bg-gray-800 border-0 py-1 px-3 focus:outline-none hover:drop-shadow-lg hover:bg-gray-700 rounded text-base mt-4 md:mt-0">Sign In
            <svg fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" class="w-4 h-4 ml-1" viewBox="0 0 24 24">
              <path d="M5 12h14M12 5l7 7-7 7"></path>
            </svg>
          </button>
        </div>
    </header>
    <section class="text-gray-600 body-font">
        <div class="container mx-auto flex px-5 py-24 items-center justify-center flex-col">
          <div class="text-center lg:w-2/3 w-full">
            <h1 class="title-font sm:text-4xl text-3xl mb-4 font-medium text-gray-900">Not Safe!</h1>
            <p class="mb-1 leading-relaxed">The link that you are trying to open can be malicious.</p>
            <p class="mb-8 leading-relaxed">You should not enter any private information like passwords, banking details etc in this website</p>
            <div class="flex justify-center">
              <button class="inline-flex text-white bg-green-500 border-0 py-2 px-6 focus:outline-none hover:bg-green-300 rounded text-lg">Go To Home Page</button>
              <button class="ml-4 inline-flex text-gray-200 bg-red-500 border-0 py-2 px-6 focus:outline-none hover:bg-red-300 rounded text-lg">Continue</button>
            </div>
          </div>
        </div>
    </section>
</body>
</html>
'''

@App.route("/search?=<query>")
def Answer(query):
  from link import Link
  from GetInfo import GetInfo

  # Webpage Code here

  '''
  If Link class raises error means that the query is not a link
  and if Link class raises error then it calls GetInfo
  '''
  try:
      any_link = Link(query)

      if any_link.is_safe():
          any_link.open()
      else:
          '''
          Flask code to display that the website is not safe and
          ask user whether to open this website or not
          '''
          # user_choosed_to_open = function_to_get_what_user_choosed()
          # if user_choosed_to_open == True:
          #     any_link.open()
          # else:
          #     '''Flask code to go back to home page'''
  except:
      info = GetInfo(query)
      Link(info['google_search_link']).open()

      # Flask code to display the info on webpage




if __name__ == "__main__":
    App.run(debug=True)
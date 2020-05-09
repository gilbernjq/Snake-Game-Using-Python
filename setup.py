import cx_Freeze

cx_Freeze.setup(
	name="SnakeGame",
	options={
				"build_exe":{
								"packages":[
											"pygame",
											"time",
											"random",
											"sys",
											"parameters",
											"playground",
											"main_game",
											"snake"
											],
											
								"include_files":[
													"ball.png",
													"food.png",
													"back.jpg",
													"instructions.png",
													"b1.png",
													"b2.png",
													"b3.png",
													"start.wav",
													"grow.wav",
													"hit.wav",
													"gameOver.wav",
													
													]
							}

			},
	description="Play Snake with python",
	executables=[cx_Freeze.Executable("playSnake.py")]
	)


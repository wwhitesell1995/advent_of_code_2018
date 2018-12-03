<?php 

include 'day_3.php';

//Tests the day_3_1 function.
function day_3_1_test()
{
	$test_val=day_3_1("day_3_test_input.txt");
	if($test_val==4)
	{
		return "Day 3_1 Test passed!".PHP_EOL;
	}
	else 
	{
		return "Day 3_1 Test failed with test value of ".$test_val.PHP_EOL;
	}
}

//Tests the day_3_2 function.
function day_3_2_test()
{
	$test_val=day_3_2("day_3_test_input.txt");
	if($test_val=="#3")
	{
		return "Day 3_2 Test passed!".PHP_EOL;
	}
	else 
	{
		return "Day 3_2 Test failed with test value of ".$test_val.PHP_EOL;
	}
}

echo day_3_1_test();
echo day_3_2_test();
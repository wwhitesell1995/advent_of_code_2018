<?php 

//Returns the number of square inches that intersect on a grid.
function day_3_1($filename)
{
	$file_lines=file($filename);
	$fabric_array=array();
	$square_inches=0;
	foreach($file_lines as $line_no=>$line)
	{
		$found_intersections=find_intersections($line, $fabric_array, $square_inches);
		$fabric_array=$found_intersections['fabric_array'];
		$square_inches=$found_intersections['square_inches'];
	}

	return $square_inches;
}

//Finds the intersections between rectangles on a grid.
function find_intersections($line, $fabric_array, $square_inches)
{
	$line=str_replace(array('#', ' '), '', $line);
	$line_array=preg_split('/(@|:|,|x)/', $line);
  for ($i=0; $i<$line_array[3]; $i++)
	{
		for($j=0; $j<$line_array[4]; $j++)
		{
			$x=$line_array[1]+$i;
			$y=$line_array[2]+$j;
			if(empty($fabric_array[$x.','.$y]))
			{
				$fabric_array[$x.','.$y]=0;
			}

			$fabric_array[$x.','.$y]+=1;
			
			if($fabric_array[$x.','.$y]==2)
			{
				$square_inches++;
			}
		}
	}

	return array('fabric_array'=>$fabric_array, 'square_inches'=>$square_inches);
}

//Returns the ID of the claim that doesn't overlap on the fabric.
function day_3_2($filename)
{
	$file_lines=file($filename);
	$fabric_array=array();
	$non_overlapping_ids=array();
	foreach($file_lines as $line_no=>$line)
	{
		$fabric_ids=find_non_overlapping_id($line, $fabric_array, $non_overlapping_ids);
		$fabric_array=$fabric_ids['fabric_array'];
		$non_overlapping_ids=$fabric_ids['non_overlapping_ids'];
	}

	if(count($non_overlapping_ids)>1)
	{
		echo "Error... More than one non-overalapping id was given!";
		return -1;
	}
	elseif(empty($non_overlapping_ids))
	{
		echo "Error... No non-overlapping id was given!";
		return -1;
	}
	
	return end($non_overlapping_ids);
}

//Finds the non-overlapping id on the grid.
function find_non_overlapping_id($line, $fabric_array, $non_overlapping_ids)
{
	$line=str_replace(array('#', ' '), '', $line);
	$line_array=preg_split('/(@|:|,|x)/', $line);
	$non_overlapping_ids[]=$line_array[0];
  for ($i=0; $i<$line_array[3]; $i++)
	{
		for($j=0; $j<$line_array[4]; $j++)
		{
			$x=$line_array[1]+$i;
			$y=$line_array[2]+$j;
			$fabric_array[$x.','.$y][]=$line_array[0];
			if(count($fabric_array[$x.','.$y])>1)
			{
				$non_overlapping_ids=array_diff($non_overlapping_ids, $fabric_array[$x.','.$y]);
			}
		}
	}

	return array('fabric_array'=>$fabric_array, 'non_overlapping_ids'=>$non_overlapping_ids);
}



echo "The number of square inches with intersections is: ".day_3_1("day_3_input.txt").PHP_EOL;
echo "The id of the claim that doesn't overlap is: ".day_3_2("day_3_input.txt").PHP_EOL;
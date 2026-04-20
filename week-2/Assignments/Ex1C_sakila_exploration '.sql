/*
a) I see the actor's ID, first and last name, and the last update
b) I see the film details like title, year and length 
c) film_actor
d) The information is easy to read as the information is labeled clearly 
e) Film ID, store ID, inventory ID, and last update
f) Rental and Inventory ID. You would look at the inventory ID and find the ID in Iventory to find the film title
*/

SELECT inventory_id FROM inventory;
SELECT rental_date FROM rental;
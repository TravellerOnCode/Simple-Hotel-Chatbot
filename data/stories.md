## Book a Room
* room_booking_direct
    - roombooking_form
    - form{"name": "roombooking_form"}
    - form{"name": null}
    
## Book a room with all info
* room_booking_immediate
    - roombooking_form
    - form{"name": "roombooking_form"}
    - form{"name": null}
    
 
## Book a room with deviation
* room_booking_direct
    - roombooking_form
    - form{"name": "roombooking_form"}
* faq_check_in
    - utter_checkin_time
    - roombooking_form
    - form{"name": null}
    
## Book a room with deviation to check out
* room_booking_direct
    - roombooking_form
    - form{"name": "roombooking_form"}
* faq_check_out
    - utter_checkout_time
    - roombooking_form
    - form{"name": null}
    

## Book a room with deviation to cancel reservation
* room_booking_direct
    - roombooking_form
    - form{"name": "roombooking_form"}
* faq_reservation_cancel
    - utter_cancel_reservation
    - roombooking_form
    - form{"name": null}
    
## Book a room with deviation to cancellation policy
* room_booking_direct
    - roombooking_form
    - form{"name": "roombooking_form"}
* faq_cancellation_policy
    - utter_cancellation_policy
    - roombooking_form
    - form{"name": null}
    
## Book a room with deviation to restaurant presence
* room_booking_direct
    - roombooking_form
    - form{"name": "roombooking_form"}
* faq_restaurant
    - utter_restaurant
    - roombooking_form
    - form{"name": null}
    
## Book a room with deviation to breakfast availability
* room_booking_direct
    - roombooking_form
    - form{"name": "roombooking_form"}
* faq_breakfast_availability
    - utter_breakfast_availability
    - roombooking_form
    - form{"name": null}
    

## Book a room with deviation to breakfast timings
* room_booking_direct
    - roombooking_form
    - form{"name": "roombooking_form"}
* faq_breakfast_timings
    - utter_breakfast_timings
    - roombooking_form
    - form{"name": null}
    
## Book a room with deviation to breakfast timings
* room_booking_direct
    - roombooking_form
    - form{"name": "roombooking_form"}
* faq_restaurant_timings
    - utter_restaurant_timings
    - roombooking_form
    - form{"name": null}
    

## schedule cleaning
* cleaning_service
    - utter_ask_clean_service
* cleaning_service_time{"booking_time":"now"}
    - action_send_clean_service  


## schedule cleaning asap
* cleaning_service_time{"booking_time":"now"}
    - action_send_clean_service  
    
##faq check in
* faq_check_in
    - utter_checkin_time
    
##faq check out 
* faq_check_out
    - utter_checkout_time
    
##faq cancel reservation
* faq_reservation_cancel
    - utter_cancel_reservation

## faq_cancellation_policy
* faq_cancellation_policy
    - utter_cancellation_policy
    
##faq restaurant presence
* faq_restaurant
    - utter_restaurant
    
##faq breakfast availability
* faq_breakfast_availability
    - utter_breakfast_availability
    
##faq_breakfast_ timings
* faq_breakfast_timings
    - utter_breakfast_timings
    
##faq_restaurant_ timings
* faq_restaurant_timings
    - utter_restaurant_timings
    

## Showing graditude
* gratitude
  - utter_gratitude

## Greet User
* greet
  - utter_greet


## happy path
* greet
  - utter_greet
* mood_great
  - utter_happy

## sad path 1
* greet
  - utter_greet
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* affirm
  - utter_happy

## sad path 2
* greet
  - utter_greet
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* deny
  - utter_goodbye

## say goodbye
* goodbye
  - utter_goodbye

## bot challenge
* bot_challenge
  - utter_iamabot

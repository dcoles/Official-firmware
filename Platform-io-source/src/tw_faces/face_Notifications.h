#pragma once

#include "tw_faces/tw_face.h"

class FaceNotifications : public tw_face
{
	public:
		void setup(void);
		void draw(bool force);
		bool click(int16_t pos_x, int16_t pos_y);
		bool click_double(int16_t pos_x, int16_t pos_y);
		bool click_long(int16_t pos_x, int16_t pos_y);

		void add_message(String message);

	private:
		String version = "1.0";
		String message_queue[4];
		uint8_t num_messages = 0;
		void pop_message();
};

extern FaceNotifications face_notifications;
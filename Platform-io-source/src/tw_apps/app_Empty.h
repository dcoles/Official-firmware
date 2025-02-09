#pragma once

#include "tw_apps/tw_app.h"

class AppEmpty : public tw_app
{
	public:
		// virtual methods
		void setup(void);
		void pre_start(void);
		void draw(bool force);
		void draw_icon(uint8_t canvasid, int16_t _pos_x, int16_t _pos_y, uint8_t style_hint);
		bool click(uint16_t click_pos_x, uint16_t click_pos_y);
		bool click_double(uint16_t click_pos_x, uint16_t click_pos_y);

		// local methods
		
	private:
		unsigned long shutdown_timer = 0;
};

extern AppEmpty app_empty;

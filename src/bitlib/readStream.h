#ifndef READ_STREAM_H
#define READ_STREAM_H

/**
 * transaction.h - Bitcoin poscript generator
 *
 * Copyright (C)2015 The bitgen developers <bitgen@openmailbox.org>
 *
 * This library is free software; you can redistribute it and/or
 * modify it under the terms of the GNU Lesser General Public
 * License as published by the Free Software Foundation; either
 * version 2.1 of the License, or any later version.
 *
 * This library is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
 * Lesser General Public License for more details.
 *
 * You should have received a copy of the GNU Lesser General Public
 * License along with this library; if not, write to the Free Software
 * Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA 02110-1301 USA
 */


#include <string>
#include <iostream>

#include "util.h"





class ReadStream
{
public:
	ReadStream(const std::string& inStr) : str(inStr), pos(0) {}
	
	unsigned char get(bool& ok)
	{
		if(pos >= str.size())
		{
			ok = false;
			return 0;
		}
		
		return str[pos++];
	}

	unsigned char peek(const int offset)
	{
		if((pos + offset) >= str.size())
		{
			throw std::string("No more data for offset");
		}
		
		return str[pos + offset];
	}

	unsigned char peek()
	{
		if(pos >= str.size())
		{
			throw std::string("No more data");
		}
		
		return str[pos];
	}



	std::string getStr(const int size)
	{
		if((pos + size) > str.size())
		{
			//std::cout << "Reguested: " << size << ", got: " << (str.size() - pos) << std::endl;
			//std::cout << "Total size: " << str.size() << std::endl;
			std::string errStr("Requested bytes count not available: ");
			errStr += intToString(size);
			
			throw errStr; //std::string("Requested bytes count not available");
		}
		
		const std::string ret = str.substr(pos, size);
		pos += size;
		return ret;
	}

	void setPos(const int newPos) 
	{
		pos = newPos;
	}

	int currentPos() const { return pos; }
	
	bool end() const { return pos == str.size(); }
	
	int remaining() const { return str.size() - pos; }
	
	std::string getFromStartWithSize(const int size) const
	{
		return str.substr(0, size);
	}
	
	std::string getFromPosWithSize(const int start, const int size) const
	{
		return str.substr(start, size);
	}
	
	int totalSize() const { return str.size(); }
	
	const std::string str;
	int pos;
};



#endif

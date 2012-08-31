# ###################################################
# Copyright (C) 2012 The Unknown Horizons Team
# team@unknown-horizons.org
# This file is part of Unknown Horizons.
#
# Unknown Horizons is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the
# Free Software Foundation, Inc.,
# 51 Franklin St, Fifth Floor, Boston, MA  02110-1301  USA
# ###################################################

from horizons.util.shapes import distances


class Shape(object):

	def distance(self, other):
		# TODO pre-build a dictionary for fast function lookup
		co1 = self.__class__.__name__.lower()
		co2 = other.__class__.__name__.lower()

		# ConstX and X are the same w.r.t to distances
		co1 = co1.replace('const', '')
		co2 = co2.replace('const', '')

		dist = getattr(distances, "distance_%s_%s" % (co1, co2), None)
		if dist:
			return dist(self, other)
		else:
			dist = getattr(distances, "distance_%s_%s" % (co2, co1), None)
			if dist:
				return dist(other, self)

		raise TypeError("No distance defined between %s and %s" % (co1, co2))

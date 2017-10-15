instance Functor Maybe where
fmap func (Just val) = Just (func val)
fmap func Nothing = Nothing